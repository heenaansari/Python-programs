n=int(input("Enter a  number : "))
k=0


for i in range(2,n):
    if(i%j==0):
        k=1
        break
if(k==0):
    print("\t ",n," is a Prime number." )
else:
    print("\t ",n," is not a Prime number.")
