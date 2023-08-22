# 0 2 8 14 24 34
n=8
i=1
pr=0
while(i<=n):
    if(i%2==0):          
        pr=(i**2)-2            #2**2-2=2  
        print(pr,end=" ")
    else:
        pr=(i**2)-1            # 1**2-1=0  
        print(pr,end=" ")
    i=i+1