# temp_conversion_tool.py

# Two global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get temperature input from user
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # Validate numeric input

        # Get unit of the temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on unit
        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function
if __name__ == "__main__":
    main()