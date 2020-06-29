# PYTHON CALCULATOR V-0.1

print("Options:")
print("Enter 'add' to add two numbers")
print("Enter 'subtract' to subtract two numbers")
print("Enter 'multiply' to multiply two numbers")
print("Enter 'divide' to divide two numbers")
print("Enter 'quit' to end the program")
user_input = str(input(": \n"))


if user_input == "quit":
    print("Thank you for using.")
      

elif user_input == "add":
    num1 = float(input("Enter number1: \n"))
    num2 = float(input("Enter number2: \n"))
    result = str(num1 + num2)
    print("\nThe answer is " + result)  
      

elif user_input == "subtract":
    num1 = float(input("Enter number1: \n"))
    num2 = float(input("Enter number2: \n"))
    result = str(num1 - num2)
    print("\nThe answer is " + result)
   

elif user_input == "multiply":
    num1 = float(input("Enter number1: \n"))
    num2 = float(input("Enter number2: \n"))
    result = str(num1 * num2)
    print("\nThe answer is " + result)
    
elif user_input == "divide":
    num1 = float(input("Enter number1: \n"))
    num2 = float(input("Enter number2: \n"))
    result = str(num1 / num2)
    print("\nThe answer is " + result)


else:

    print("\nUnknown input")


    
