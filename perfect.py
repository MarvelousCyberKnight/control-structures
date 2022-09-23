n=int(input())
count=0
temp=n
for i in range(1,n):
    if n%i==0:
        count=count+i
if temp==count:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
