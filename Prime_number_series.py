n=int(input("Enter a  number : "))
k=0
for i in range(2,n+1):
    for j  in range(2,i):
        if(i%j==0):
            k=1
            break
    if(k==0):
        print("\t",i,end="")
    k=0
