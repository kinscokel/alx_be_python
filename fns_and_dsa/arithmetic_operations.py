# arithmetic_operations.py
def perform_operation(num1, num2, operation):
    """ executes this opeartional functions!"""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtraction':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    if operation == 'division':
        if num2 == 0:
            return "Error: non operational"
        return num1 / num2
    else:
        return "Error: inavalid operation"
