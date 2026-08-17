print("Give me a name and age") 
name = input("what your name") 
age = input("whats your age")  
print(name, age)
age_as_int = int(age) 

if age_as_int > 100:
	print("false") 
elif age_as_int > 0: 
	print("ahah") 
else: 
	print("oooo")
