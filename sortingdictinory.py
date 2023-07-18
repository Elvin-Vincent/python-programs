d={}
n=int(input("enter the number of numbers:"))
for i in range(n):
    name=input("enter the names")
    rollno=int(input("\nenter the rollnumber"))
    d[rollno]=name
names=sorted(d.values())
for i in names:
    print(i)