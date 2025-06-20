# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that adds two numbers.
        Doesn't access class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that multiplies two numbers.
        Accesses class attribute 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(5, 3)
    print(f"Sum: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(5, 3)
    print(f"Product: {product_result}")