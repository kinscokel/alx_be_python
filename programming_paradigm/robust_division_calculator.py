# File: robust_division_calculator.py import safe_divide
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"Result: {result}"
    except ValueError:
        return "Error: Please enter numeric values."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

            
            

        



            