print("increasing")
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
n=5
print("decreasing")
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()