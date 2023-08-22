# 0 2 6 12 ... N The square term minus the original iteration value
n=int(input("Enter the limit : "))
i=1
sum=0
while(i<=n):
    print((i*i)-i,end=" ") #2*2-2 = 4-2=2   #3*3-3=9-3=6 
    i=i+1
    
    