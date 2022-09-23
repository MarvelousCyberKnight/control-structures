n=int(input())
for i in range(1,n+1):
    if i%2==0:
        a=(i**2)-2
        print(a,end=' ')
    else:
        a=(i**2)-1
        print(a,end=' ')
