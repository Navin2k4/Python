vow=['a','e','i','o','u','A','E','I','O','U']
string=input("Enter the string :")
count=0
ucount=0
lcount=0
for letter in string:
    if letter.isupper():
        ucount+=1
    elif letter.islower():
        lcount+=1
    else:
        count+=1
print("Upper Cases = ",ucount)
print("Lower Cases = ",lcount)
print("Other Characters = ",count)
