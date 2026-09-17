# Take two number from the user, add it and display it


# num1 = int(input("Enter the first number : ")) # 10
# num2 = int(input("Enter the second number : ")) # 10

# sum = num1 + num2 # 1010
# print(sum)

# print()
name = "Priyanshu"
age = 21

# Hello everyone! My name is Priyanshu and age is 21
print("Hello everyone! My name is", name, "and age is", age,sep=" ", end="\n") # commas
print("Hello everyone! My name is " + name + " and age is " + str(age)) # concatenation
print("Hello everyone! My name is %s and age is %d"%(name, age)) # % formatting
print("Hello everyone! My name is {} and age is {}".format(name, age)) # str.format()
print(f"Hello everyone! My name is {name} and age is {age}") # f-string