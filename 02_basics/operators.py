# Arithmatic operator : +, -, *, /, //, %, **
a = 16
b = 5

print(a + b) # 21
print(a - b) # 11
print(a * b) # 80
print(a / b) # 3.2
print(a // b) # 3
print(a % b) # 1
print(a ** b) # 1048576

# Assignment operator : =, +=, -=, *=, /=, //=, %=, **=
x = 10
y = 20

x += y
print(x) # 30

# Comparison operator : >, >=, <, <=, !=, ==
x = 10
y = 10

print(x > y) # False
print(x >= y) # True
print(x < y) # False
print(x <= y) # True
print(x != y) # False
print(x == y) # True

print("-------------------------------------------------")

# Membership operator : in, not in
my_list = [10, 20, 32, 43, "Hello"]
b = "Hello"

print(b in my_list) # True
print(b not in my_list) # False


print("----------------------------")

# Identity operator : is, is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # True
print(a is c) # False
print(a == c) # True
print("%.3f"%(10/3))
