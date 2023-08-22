#Amstrong  number
n=int(input("Enter a number : "))
sum=0
i=1
num=n
while(n>0):
    rem=n%10
    sum=(sum)+rem
    n=n//10
print("The reversed number is : ",sum)
    
