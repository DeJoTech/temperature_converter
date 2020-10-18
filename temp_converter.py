# Simple temperature conversion script to calculate between Celsius, Fahrenheit,
# and Kelvin determined by user input.


def fahrenheit_to_celsius(celsius):
    """Accepts Fahrenheit temp from input and converts it to Celsius"""
    celsius = ((float(celsius) - 32) * 5 / 9)
    return celsius


def fahrenheit_to_kelvin(kelvin):
    """Accepts Fahrenheit temp from input and converts it to Kelvin"""
    kelvin = (float(kelvin)-32) * 5/9 + 273.15
    return kelvin


def celsius_to_fahrenheit(fahrenheit):
    """Accepts Celsius temp from input and converts it to Fahrenheit"""
    fahrenheit = ((float(fahrenheit) * 9 / 5) + 32)
    return fahrenheit


def celsius_to_kelvin(kelvin):
    """Accepts Celsius temp from input and converts it to Kelvin"""
    kelvin = float(kelvin) + 273.15
    return kelvin


def kelvin_to_fahrenheit(fahrenheit):
    """Accepts Kelvin temp from input and converts it to Fahrenheit"""
    fahrenheit = (float(fahrenheit)-273.15) * 9/5 + 32
    return fahrenheit


def kelvin_to_celsius(celsius):
    """Accepts Kelvin temp from input and converts it to Celsius"""
    celsius = float(celsius) - 273.15
    return celsius


CONVERTERS = {'CF': celsius_to_fahrenheit,
              'FC': fahrenheit_to_celsius,
              'KC': kelvin_to_celsius,
              'CK': celsius_to_kelvin,
              'FK': fahrenheit_to_kelvin,
              'KF': kelvin_to_fahrenheit
              }


def convert():
    """Accepts temperature and conversion scale inputs from user then runs the
    temperature through the conversion process."""

    try:
        temperature = input("Enter temperature for conversion. Example 98.8 F: ").split(' ')
        scale = input("Convert to: C (celsius) F (fahrenheit) K (kelvin): ").upper()
        convert_code = temperature[1].upper() + scale
        result = CONVERTERS[convert_code](float(temperature[0]))
        print(f"{temperature[0]}° {temperature[1].upper()} = {result:.1f}° {scale}")
    except KeyError:
        print("Invalid Scale: Enter scale as C, F, or K")
    except (ValueError, IndexError):
        print("Invalid Format: Format example 98.6 F")


if __name__ == '__main__':
    convert()
