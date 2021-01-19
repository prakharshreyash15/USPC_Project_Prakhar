# Project - Uber Shortest Path Computation - SWE Internship
# Microtask 1
x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))
D= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
print("distance between",(x1,x2),"and",(y1,y2),"is : ",D)