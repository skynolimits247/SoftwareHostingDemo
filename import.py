import csv
import sys
import os
import xlrd
project_dir = "C:\hosting\hosting"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()
from home.models import win_64

data= "c:\hosting\software-desc.xlsx"
print "here"
workbook = xlrd.open_workbook(data)
sheet=workbook.sheet_by_index(0)
print "here"
tcol=sheet.ncols
trow=sheet.nrows
for x in range(trow):
     software_des = win_64()
     for y in range(tcol):
          
          print 'y= ',y,'value= ',sheet.cell(x,y).value
          if y==0:
               software_des.name = sheet.cell(x,y).value
          #print' row1= ',row[1]
          sheet.cell(x,y).value
          if y == 1:
               software_des.link = sheet.cell(x,y).value
          y+=1
     x+=1
     software_des.save()
          
         

          



    
    
