# I want to see every keyword in python

import keyword
kw_list = keyword.kwlist
print(kw_list)


# Check a word is keyword or not
print(keyword.iskeyword('Falsewe'))


# Declare and initialize the variable

number = 10
numberFloat = 45.7
name = "Rishi"
cmpNum = 6 + 9j
isPrime = True
my_list = [56, 76, 76.7, True, 7 + 5j]
my_tuple = (56, 76, 76.7, True, 7 + 5j)
my_set = {56, 76, 76.7, True, 7 + 5j}
my_dict = {"name" : "Arpit", "age":20, "city": "Pune"}

print(number, type(number), numberFloat, type(numberFloat), name, type(name)) # Output : 10, data type -> int
print(numberFloat, type(numberFloat)) # Output : 45. 7, float
# print(name, type(name)) # Output : Rishi, str 
# print(cmpNum, type(cmpNum)) # Output : 6 + 9j, complex
# print(isPrime, type(isPrime)) # Output : True, bool
# print(my_list, type(my_list)) # Output : [56, 76, 76.7, True, 7 + 5j], list
# print(my_tuple, type(my_tuple)) # Output : (56, 76, 76.7, True, 7 + 5j), tuple
# print( my_set, type(my_set)) # Output : {56, 76, 76.7, True, 7 + 5j}, set
# print( my_dict, type(my_dict)) # Output : {"name" : "Arpit", "age":20, "city": "Pune"}, dict