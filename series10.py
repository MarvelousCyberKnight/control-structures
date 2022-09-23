n=int(input())
a=95.0
count=20.5
print(a,end=' ')
for i in range(1,n):
    b=a+count
    print(b,end=' ')
    a=b
    count=count+2.0
