string=input("Enter a String")
string_list=string.split(" ")
length=[]
print(string_list)
for words in string_list:
    length.append(len(words))
print(length)
x=length.index(max(length))
print("The largest letter is",string_list[x])
print("The length of letter is",length[x])


    

    
