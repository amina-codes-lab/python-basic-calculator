num1 = float(input("Enter first number = "))
operator = input("Enter any operator(+,-,/,*): ")
num2 = float(input("Enter second number = "))
if operator == "+":
    print(num1, "+", num2, "=", num1+num2)
elif operator == "-":
    print(num1, "-", num2, "=", num1-num2)
elif operator == "*":
    print(num1, "*", num2, "=", num1*num2)
elif operator == "/":
    if num2 == 0:
        print("Invalid! Cannot divide by zero.")
    else:
        print(num1, "/", num2, "=", num1/num2)
else:
    print("Invalid Operator")