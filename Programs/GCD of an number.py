#Gcd of a number
a=int(input("Enter number 1 : "))
b=int(input("enter number 2 : "))
if(a>b):
    divident=b
    divisor=a
else:
    divident=a
    divisor=b
while(divisor!=0):
    rem=divident%divisor
    divident=divisor
    divisor=rem
print(divident)
