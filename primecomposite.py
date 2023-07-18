list=[3,4,6,7,9]
primelist=[]
compolist=[]

for i in list:
    flag=0
    for n in range (2,i):
        if(i%n==0):
           flag=1
           break
    if flag==0:

        primelist.append(i)
    else:
        compolist.append(i)
print("primenumber",primelist)
print("\ncompositenumber",compolist)
        
