def nametag(first_name, last_name):
	result="{} {}.".format(first_name,last_name[0])
	return result

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 