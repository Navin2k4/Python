#Amstrong  number
n=int(input("Enter a number : "))
sum=0
i=1
num=n
while(n>0):
    rem=n%10
    sum=sum+rem**3
    n=n//10
print(sum)
if(sum==num):
    print("The given number is armstrong number ")
else:
    print("The given number is not armstrong number")
    