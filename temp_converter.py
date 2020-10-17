# Simple temperature conversion script to calculate (°C to °F) or (°F to °C).


def fahrenheit_to_celsius(celsius):
    """Accepts Fahrenheit temp from input and converts it to Celsius"""
    celsius = ((float(celsius) - 32) * 5 / 9)
    return celsius


def celsius_to_fahrenheit(fahrenheit):
    """Accepts Celsius temp from input and converts it to Fahrenheit"""
    fahrenheit = ((float(fahrenheit) * 9 / 5) + 32)
    return fahrenheit


CONVERTERS = {'C': celsius_to_fahrenheit,
              'F': fahrenheit_to_celsius}


def convert():
    """Accepts temperature input from user then runs the temperature
    through the conversion process."""
    try:
        temperature = input("Enter temperature for conversion example 98.8 F, 36.7 C: ").split(' ')
        scale = 'F' if temperature[1].upper() == 'C' else 'C'
        result = CONVERTERS[temperature[1].upper()](float(temperature[0]))
        print(f"{temperature[0]}°{temperature[1].upper()} = {result:.1f}°{scale}")
    except KeyError:
        print("Invalid Scale: Enter scale as C or F")
    except (ValueError, IndexError):
        print("Invalid Format: Format example 98.6 F or 36 C  ")


if __name__ == '__main__':
    convert()
