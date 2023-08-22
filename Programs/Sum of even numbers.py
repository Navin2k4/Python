n=int(input("Enter the number of terms n : "))
print("The number of terms are , ",n)
sum=0
for i in range(0,n):
    if(i%2==0):
        sum=sum+i
    
print(sum)