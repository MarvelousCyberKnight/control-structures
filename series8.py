n=int(input())
a=4
print(a,end=' ')
for i in range(1,n):
    b=a+i*i
    print(b,end=' ')
    a=b
