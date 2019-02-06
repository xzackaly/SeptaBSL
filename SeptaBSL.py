# add color to Septa Broad Street Line chart
#  to distinguish the 8th & Market and Express trains 
#   

import re

rx_dict ={'timecell': re.compile('<tr><td>')}

def _parse_line(line):
 
    # Do a regex to find all time cells in the Septa BSL chart
 
    for k, v in rx_dict.items():
        match = v.findall(line)
        if match:
            return k, match
    # if there are no matches
    return None, None

#set up file variables 
fileout_name = "septaout.htm"
outfile = open(fileout_name, 'w')
Septa_in = open('BSL_0.txt','r')

#set up program variables   
timerow = []
timecells = []
testtrace = 0
color8th = ' style="background-color: #FAB935;"'
colorxprss = ' style="background-color: #77F34F;"'

greencells = (8,12,17,20,23,26,29,32,35,38,41,44,47,50,53,56,59,
62,65,68,71,74,77,80,83,86,89,92,95,99,
101,105,108,112,114,118,121,125,127,131,134,138,140,144,147,
151,153,157,160,164,166,170,173,177,179,183,186,190,193,198,
201,204,207,210,213,216,219,222,225,228,231,234,237,240,243,246,249,252,255,258)

yellowcells = (4,6,10,13,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,
60,63,66,69,72,75,78,81,84,87,90,94,97,
103,107,110,116,120,123,129,133,136,142,146,149,
155,159,162,168,172,175,181,185,188,191,194,196,199,
202,205,208,211,214,217,220,223,226,229,232,235,238,
241,244,247,250,253,256,259,261,263,266,269,272,275,278)

tintLine = 0

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
               
                
                colorline = timerow[0]
          
                for cellindex in range(len(timecells) - 1,-1,-1): 
                     endpos = timecells[cellindex]
                     endpos_1 = endpos - 1
                     if (cellindex + 1) in yellowcells:
                        colorline = colorline[:endpos_1] + color8th + colorline[endpos_1:]
                        tintLine = 1
                     if (cellindex + 1) in greencells:
                        colorline = colorline[:endpos_1] + colorxprss + colorline[endpos_1:]
                        tintLine = 1
             

            if tintLine == 1:
                outfile.write(colorline)  
                tintLine = 0 
            else:    
                outfile.write(line_in)

            line_in = file_object.readline()

Septa_in.close()
outfile.close()


print ("***End Of Septa Process***")
