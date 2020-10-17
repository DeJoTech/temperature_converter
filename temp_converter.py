# Simple temperature conversion script to calculate (°C to °F) or (°F to °C).

def fahrenheit_to_celsius(celsius):
    """Accepts Fahrenheit temp from input and converts it to Celsius"""
    celsius = ((float(celsius) - 32) * 5 / 9)
    return celsius


def celsius_to_fahrenheit(fahrenheit):
    """Accepts Celsius temp from input and converts it to Fahrenheit"""
    fahrenheit = ((float(fahrenheit) * 9 / 5) + 32)
    return fahrenheit


def convert_scale(_scale):
    """Converts the scale from °C to °F or vise versa for display in final output"""
    if _scale.upper() == "C":
        _scale = "F"
    elif _scale.upper() == "F":
        _scale = "C"
    return _scale


scale = input("Enter C to convert Celsius or F to convert Fahrenheit: ")

if scale.upper() == "C" or scale.upper() == "F":
    temperature = input(f"Enter {scale.upper()} temperature for conversion: ")
    scale_conversion = convert_scale(scale)
    if scale.upper() == "C":
        temp_conversion = celsius_to_fahrenheit(temperature)
        print(f"The temperature is {temp_conversion:.1f}° {scale_conversion}")
    elif scale.upper() == "F":
        temp_conversion = fahrenheit_to_celsius(temperature)
        print(f"The temperature is {temp_conversion:.1f}° {scale_conversion}")
else:
    print("Invalid Option: Did not choose C or F for conversion.")
    quit()
