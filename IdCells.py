# 
import optparse
import re
import csv
from bslwork import bslwork


parser = optparse.OptionParser("""Usage: %prog [options]""")
parser.add_option("-d", "--direction", 
                      action="store", dest="direction",
                      default="sb", 
                      help="value is sb or nb (southbound or northbound) [default %default]")
parser.add_option("-t", "--typesched",
                      action="store", dest="schedule",
                      default="wd", help="value is wd or we (weekday or weekend schedule) [default %default]")

(opts, args) = parser.parse_args()

###
# get the file dependent variables and
# set up file inputs and outputs 
###
workval = bslwork(opts.direction, opts.schedule)
print ("\ncall to bslwork = ", workval)

###
###  set regex values
### 
 
numpattern = r"\d" 
 
rx_dict ={'timecell': re.compile('<tr><td>')}

def _parse_line(line):
 
    #  regex to find all time cells in the Septa BSL chart
 
    for k, v in rx_dict.items():
        match = v.findall(line)
        if match:
            return k, match
    # if there are no matches
    return None, None

###
# get the file dependent variables and
# set up file inputs and outputs 
###

runtype = workval[0]
filein_name = workval[1]
Septa_in = open(filein_name,'r')

fileout1_name = workval[2]   
f1 = open(fileout1_name, 'w')
col1 = workval[4][0]

if runtype == 'wd':
  fileout2_name = workval[3]  
  f2 = open(fileout2_name, 'w')
  col2a = workval[4][1]
  col2b = workval[4][2]

###
#set up main process variables   
##
timerow = []
timecells = []
 
list8th = []
listexpress = []


#Main Process
with Septa_in as file_object:
    line_in = file_object.readline()
   
    while line_in:
            # at each line check for a match with rdict
           
            key, match = _parse_line(line_in)
            
            if key: 
               
                timerow.append(line_in) 
                timecells.append([])
                it = re.finditer("<tr><td>", line_in)
                for m in it:     
                   timecells[(len(timerow)-1)].append(m.end())
                   
 
            line_in = file_object.readline()

##
##  Finished main process, now build list of cell numbers
##
#find 8th & Market Cell numbers
for x in range(len(timecells[col1])):   
  #if 8th&Mkt cell contains a numeric value, save the cell number
    spos =  (timecells[col1] [x])
    epos = spos + 10
    digicheck = (timerow[col1])[spos:epos] 
    if re.search(numpattern, digicheck):
        list8th.append(x)
       
#find ExpressTrain Cell numbers
if runtype == 'wd': 
  for x in range(len(timecells[col2a])):   
  #if Walnut-Locust contains a numeric value, and Lombard cell does not  
  # have a numeric value, save the cell number
    spos =  (timecells[col2a] [x])
    spos2 =  (timecells[col2b] [x])
    epos = spos + 10
    epos2 = spos2 + 10
    digicheck = (timerow[col2a])[spos:epos] 
    digicheck2 = (timerow[col2b])[spos2:epos2] 
    if re.search(numpattern, digicheck):
        if not re.search(numpattern, digicheck2):
            listexpress.append(x)

##
##  Close the input, write output  
##      
Septa_in.close()

writer1 = csv.writer(f1)
writer1.writerow(list8th) 

if runtype == 'wd': 
  writer2 = csv.writer(f2)
  writer2.writerow(listexpress)
 

print ("\n***End Of ID Septa cells***")
