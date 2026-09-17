name = 'Mani'
name2 = "Sudhanshu"
name3 = '''
        This is my multi line string
        We are writing in triple single quote
'''
name4 = """
    This is also my multipline string 
    I am writing it in a triple double qoute
"""

print(name, type(name))
print(name2, type(name2))
print(name3, type(name3))
print(name4, type(name4))


my_list = [56, 76, 76.7, True, 7 + 5j, 76]
my_list[1] = 100
print(my_list)

my_set = {56, 76, 76.7, True, 7 + 5j, 76}
print(my_set)

x = 10
y = 10.5

z = x + y
print(z, type(z)) # Output : 20.5, float ---> Implicit type conversion

# Explicit type conversion
name = "ABC"
age = 20
msg = "Hello everyone, my name is " + name + " and I am " + str(age) + " years old."
print(msg)

# Different type conversion functions
# int() - converts a value to an integer
# float() - converts a value to a float
# str() - converts a value to a string
# bool() - converts a value to a boolean
# list() - converts a value to a list
# complex() - converts a value to a complex number
# set() - converts a value to a set
# tuple() - converts a value to a tuple
# dict() - converts a value to a dictionary

mes = "23.5"
value1 = float(mes)
print(value1, type(value1)) # Error: ValueError: invalid literal for int() with base 10: '23.5'