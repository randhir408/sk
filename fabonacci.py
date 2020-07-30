num=int(input("enter the number=="))
i=1
a=0
b=1
while i<=num:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i=i+1