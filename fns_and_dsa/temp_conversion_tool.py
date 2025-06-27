# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion from Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Conversion from Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temp = float(temp_input)  # Raises ValueError if not a number
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        elif unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        else:
            print("Invalid input. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the script
if __name__ == "__main__":
    main()

