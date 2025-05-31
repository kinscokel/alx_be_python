#  match_case_calculator.py

# prompt user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# prompt user for an operation
operation = input("choose the operation (+): ")

# perform calculation using match case
match operation:
    case '+':
      result = num1 + num2    
      
      print(f"The result is {result}. ")

