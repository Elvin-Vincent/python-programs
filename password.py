s=input("enter the password:")
l=0
u=0
n=0
spcl=0
if (len(s)>=6):
    for i in s:
        if(i.islower()):
            l=l+1
        if(i.isupper()):
            u=u+1
        if(i.isdigit()):
            n=n+1
        if(i=='$'or i=='@' or i=='#'):
            spcl=spcl+1
if(l>0 and u>0 and n>0 and spcl>0 and l+u+n+spcl==len(s)):
    print("valud password")
else:
    print("wrong password")

