n=int(input())
a=1
print(a,end=' ')
for i in range(2,n+1):
    if i%2==0:
        b=a*2
        print("%.1f"%b,end=' ')
        a=b
    else:
        b=a*3/2
        print("%.1f"%b,end=' ')
        a=b
