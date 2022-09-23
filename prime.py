n= int(input())
if n>0:
    for i in range(2,n):
        if n%i==0:
            print("Not a Prime")
            break
    else:
        print("Prime Number")
