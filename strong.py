n=int(input())
w=n
fact=1
sum=0
while(n!=0):
    digit=n%10
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if w == sum:
    print("Strong Number")
else:
    print("Not a Strong Number")
