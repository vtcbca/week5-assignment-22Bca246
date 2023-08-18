# Write a python program create csv file student.csv(sid,sname,city,contact) using 10 records 
##(in which 5 records input directly and 5 records take input from user). write records into this file.

import csv
r=open('c:\\22bca246\\stud.csv','w',newline='')
w=csv.writer(r)
header=['sid','sname','city','contact']
w.writerow(header)
rows=[[1,'shivu','mumbai',7835657845],[2,'krishna','dwarka',9456745612],[3,'radhe','vrindavan',7465645345],[4,'omii','surat',5675548454],[5,'madhav','mathura',5464384545]]
w.writerows(rows)
l=[]
for x in range(1):
    j=int(input("Enter student id:"))
    i=input("Enter student name:")
    y=input("Enter city:")
    u=int(input("Enter contact number:"))
    list=[j,i,y,u]
    l.append(list)
    w.writerows(l)
 r.close()
 from csv import DictReader
 with open('c:\\22BCA246\\stud.csv','r',newline='')as o:
    a=DictReader(o)
    for row in a:
        print(row)
