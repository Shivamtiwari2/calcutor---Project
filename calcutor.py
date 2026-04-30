print("calculator")

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
num3 = float(input("Enter third number"))

print("1. Add")
print("2. Subtract")
print("3.Multply")
print("4. Divide")
print("5.%")

choice = input("Choose option:")

if choice == "1":
    print("Result =", num1 + num2 + num3)

elif choice == "2":
    print("Result =", num1 - num2 - num3)

elif choice == "3":
    print("Result =", num1 * num2 * num3)

elif choice == "4":
    print("Result =", num1 / num2 / num3)

elif choice == "5":
    print("Result =", num1 % num2 % num3)

else:
    print("Invald choice")

again = input("Do you want to calculate again? (yes/no):")
print(again)



