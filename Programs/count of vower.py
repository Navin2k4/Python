vow=['a','e','i','o','u','A','E','I','O','U']
string=input("Enter the string :")
count=0
for letter in string:
    if letter in vow:
        count+=1
        print(letter,end=" ")
print(count)