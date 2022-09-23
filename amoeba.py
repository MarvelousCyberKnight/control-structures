n=int(input("Enter the number of months \n"))
a=-1
b=1
for i in range(1,n+1):
        c=a+b
        a=b
        b=c
print("The amoeba size is %d"%c)
