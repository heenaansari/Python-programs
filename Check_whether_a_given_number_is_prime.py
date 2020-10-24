n=int(input("Enter a  number : "))
k=0


for i in range(2,n):
    if(n%i==0):
        k=1
        break
if(n==1 or n==0):
    print("Niether a prime number nor composite")
else:
    if(k==0):
        print("\t ",n," is a Prime number." )
    else:
        print("\t ",n," is not a Prime number.")
