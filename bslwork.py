#!/usr/bin/env python

def bslwork(direction, schedtype):
    t1 = "_8th.txt"
    t2 = "_xprs.txt"
    f2 = fbslin = None
    if schedtype == 'wd': 
      f2 = "%s%s%s" % (schedtype,direction,t2)
      if direction == 'sb':
         fbslin = 'BSL0.txt'
         cols = (12, 17, 18)
      if  direction == 'nb':
         fbslin = 'BSL1.txt'
         cols = (10, 6, 5)
      
    if schedtype == 'we': 
      if direction == 'sb':
         fbslin = 'BSL0we.txt'
         cols = (12)
      if direction == 'nb':
         fbslin = 'BSL1we.txt'  
         cols = (10)  

    f1 =  "%s%s%s" % (schedtype,direction,t1)
     

    return (schedtype, fbslin, f1, f2, cols )

 