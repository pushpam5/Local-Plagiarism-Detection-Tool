from math import sqrt,acos,cos
file1=open(filename1,'r')
file2=open(filename2,'r')
fl1=file1.read().split()
fl2=file2.read().split()
dict_file1={}
dict_file2={}
for i in fl1:
    if i not in dict_file1:
        dict_file1[i.lower()]=0  
    dict_file1[i.lower()]+=1
for i in fl2:
    if i not in dict_file2:
        dict_file2[i.lower()]=0
    dict_file2[i.lower()]+=1


sum1=sum(i*i  for i in dict_file1.values())
sum2=sum(i*i  for i in dict_file2.values())
mod_fl1=sqrt(sum1)
mod_fl2=sqrt(sum2)
dotProduct=0
for key in dict_file2:
    if key in dict_file1:
        dotProduct+=dict_file1[key]*dict_file2[key]
distance=acos(dotProduct/int(mod_fl1*mod_fl2))
if distance==0:
     print("Complete Match found")
elif distance>0 and distance<= (1/sqrt(2)): //setting the threshold to 45 degrees
    print("Partial Match Found")
else:
    print("No Match Found")
file2.close()
file1.close()
