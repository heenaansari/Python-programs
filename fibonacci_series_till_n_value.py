n=int(input("Enter a number = "))
fibo=[0,1]
for i in range(2,n+1):
    x=fibo[i-1]+fibo[i-2]
    if(x<=n):
        fibo.append(x)
    
print(fibo)
