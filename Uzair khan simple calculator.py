print (' Bot: I am a simple calculator')
print("Select an operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation =input()
if operation=="1":
    num1=input("enter first number:  ")
    num2=input("enter second number:  ")
    print("the result is " + str(int(num1) +int(num2)))
elif operation=="2":
    num1=input("enter first number: ")
    num2=input("enter second number: ")
    print("the result is " + str(int(num1) - int(num2)))
elif operation=="3":
    num1=input("enter first number: ")
    num2=input("enter second number: ")
    print("the result is " + str(int(num1) * int(num2)))
elif operation=="4":
     num1=input("enter first number: ")
     num2=input("enter second number: ")
     print("the result is " + str(int(num1) / int(num2)))


else:
    print("invalid entry")

