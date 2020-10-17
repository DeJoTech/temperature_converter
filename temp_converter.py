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
    temperature = input("Enter temperature for conversion example '98.8 F', '36.7 C': ")
    scale = temperature[-1:].upper()
    degree_scale = 'F' if scale.upper() == 'C' else 'C'
    temp_val = temperature.split(' ')
    result = CONVERTERS[scale](float(temp_val[0]))
    print(f"{temperature} = {result:.1f} °{degree_scale}")


if __name__ == '__main__':
    convert()
