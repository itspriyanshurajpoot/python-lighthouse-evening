





print("Press 1 for calculator calculation")
print("Press 2 for annual salary calculation")
print("Press 3 for SI calculation")
choice = int(input())

# if (choice == 1) :
#     num1 = int(input("Enter the first number : "))
#     num2 = int(input("Enter the second number : "))

#     add = num1 + num2
#     sub = num1 - num2
#     mul = num1 * num2
#     div = num1 / num2

#     print("Sum is ", add)
#     print("Subtraction is ", sub)
#     print("Product is ", mul)
#     print("Division is ", div)
# else:
#     if(choice == 2):
#         salary = int(input("Enter the salary"))
        
#         annual = 12 * (salary + (salary * 0.1))
#         print("Annual salary is", annual)
#     else:
#         if(choice == 3):
#             p = int(input("Enter the principal amount "))
#             r = float(input("Enter the rate of interest "))
#             t = float(input("Enter the time(in year) "))

#             si = p * r * t/100
#             print("Simple intrest is ", si)
#         else:
#             print("Invalid choice")


if choice == 1 :
    # calculator
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    print("Sum is ", add)
    print("Subtraction is ", sub)
    print("Product is ", mul)
    print("Division is ", div)

elif choice == 2:
    # annual calary
    salary = int(input("Enter the salary"))
            
    annual = 12 * (salary + (salary * 0.1))
    print("Annual salary is", annual)

elif choice == 3:
    # SI
    p = int(input("Enter the principal amount "))
    r = float(input("Enter the rate of interest "))
    t = float(input("Enter the time(in year) "))

    si = p * r * t/100
    print("Simple intrest is ", si)

else:
    # Invalid choice 
    print("Invalid choice")