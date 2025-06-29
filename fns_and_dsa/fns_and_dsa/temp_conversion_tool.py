# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    Formula: (F - 32) x 5/9
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    Formula: (C x 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")

    # Ask user for temperature input
    temp_input = input("Enter the temperature to convert: ")

    try:
        # Try converting the input to a float
        temperature = float(temp_input)
    except ValueError:
        # Raise an error if the input is not a valid number
        print("Invalid temperature. Please enter a numeric value.")
        return  # Exit the function early

    # Ask user for the temperature unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        # Convert from Fahrenheit to Celsius
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted:.2f}°C")
    elif unit == "C":
        # Convert from Celsius to Fahrenheit
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted:.2f}°F")
    else:
        # Handle invalid unit entry
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Run the main function
if __name__ == "__main__":
    main()