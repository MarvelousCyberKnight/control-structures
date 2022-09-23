n1=int(input())
n2=int(input())
count=0
count1=0
for i in range(1,n1+1):
    if n1%i==0:
        count=count+i
for i in range(1,n2+1):
    if n2%i==0:
        count1=count1+i
if count/n1 == count1/n2:
    print("Friendly Pair")
else:
    print("Not Friendly Pair")
