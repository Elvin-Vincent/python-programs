list=[123,23.5,'hello',5]
listd=[]
lists=[]
listf=[]
for i in list:
    if type(i)==int:
        listd.append(i)
    if type(i)==str:
        lists.append(i)
    if type(i)==float:
        listf.append(i)
print("integer list:",listd)
print("\nstring list:",lists)
print("\nfloat list",listf)