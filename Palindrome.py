import math
n=int(input("Enter A String"))
t=n
s=0
for i in range(int(math.log10(n))+1):
    print(i,end=" ")
    r=t%10
    print(r,end=" ")
    s=s*10+r
    print(s,end=" ")
    t=t//10
    print(t,end=" ")
    print(".")
print(s==n)
