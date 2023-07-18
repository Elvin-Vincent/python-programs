s=input("enter the string")
n=int(len(s)/2)
firsthalf=s[0:n]
secondhalf=s[n:]
print("firsthalf:",firsthalf,"\nsecound half",secondhalf)
rfirsthalf=firsthalf[::-1]
rsecondhalf=secondhalf[::-1]
rstringfs=rfirsthalf+rsecondhalf
print(rstringfs)