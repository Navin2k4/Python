#Sum of the series
n=3
s=0
sum=0
for i in range(0,n):
    s=s*10+5
    print(s,end=" ")
    sum=sum+s
print()
print(sum)