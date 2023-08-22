#factorial of a number
n=int(input("Enter a number : "))
print("The factorial of the number is ....")
i=1
sum=1
if(n==1):
    print("The factorial of the number is 1")
else:
    while(i<=n):
        sum=sum*i
        i=i+1
    print(sum)