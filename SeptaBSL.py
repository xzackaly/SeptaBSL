# add color to Septa Broad Street Line chart
#  to distinguish the 8th &Market and Express trains 
#   

import re


# get cell numbers
#
f = open('wdsb_8th.txt', 'r')
x = f.read().split(",")
f.close() 
cells8th = []
for i in range(len(x)):
    num_2_int = int(x[i])
    cells8th.append(num_2_int)
 
f = open('wdsb_xprs.txt', 'r')
x = f.read().split(",")
f.close() 
cellsexpress = []
for i in range(len(x)):
    num_2_int = int(x[i])
    cellsexpress.append(num_2_int)



# Do a regex to find all time cells in the Septa BSL chart
rx_dict ={'timecell': re.compile('<tr><td>')}

def _parse_line(line):
 
 
    for k, v in rx_dict.items():
        match = v.findall(line)
        if match:
            return k, match
    return None, None

#set up file variables 
fileout_name = "septaout.htm"
outfile = open(fileout_name, 'w')
 
Septa_in = open('BSL_0.txt','r')

#set up program variables   
timerow = []
timecells = []
 
color8th = ' style="background-color:#FAB935"'
colorxprss = ' style="background-color:#77F34F"'

tinted = 0

#main process  
with Septa_in as file_object:
    line_in = file_object.readline()
   
    while line_in:
            # at each line check for a match with rx_dict
           
            key, match = _parse_line(line_in)
            
            if key: 
                timerow = []
                timerow.append(line_in)
                timecells = []
    

                # isolate each time cell
                it = re.finditer("<tr><td>", timerow[0])
                for m in it:     
                   timecells.append(m.end())
               
                
                workline = timerow[0]
          
                for cellindex in range(len(timecells) - 1,-1,-1): 
                     endpos = timecells[cellindex]
                     endpos_1 = endpos - 1
                     if (cellindex) in cells8th:
                        workline = workline[:endpos_1] + color8th + workline[endpos_1:]
                        tinted = 1
                     if (cellindex) in cellsexpress:
                        workline = workline[:endpos_1] + colorxprss + workline[endpos_1:]
                        tinted = 1
             

            if tinted == 1:
                outfile.write(workline)  
                tinted = 0 
            else:    
                outfile.write(line_in)

            line_in = file_object.readline()

Septa_in.close()
outfile.close()

print ("***End Of Septa Process***")
