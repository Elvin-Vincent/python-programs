vowels="AEIOUaeiou"
s=input("enter the sting:")
n=""
c=0
for i in s:
    if i not in vowels:
        n=n+i
        c=c+1
print("string without vowels:",n,"\nnumber of vowels",len(s)-c)