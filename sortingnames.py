n=int(input("enter the number of names:"))
names=[]
for i in range(n):
    nam=input("enter the name:")
    names.append(nam)
    names.sort()
print("the sorted names:\n")
for i in names:
    print(i)
