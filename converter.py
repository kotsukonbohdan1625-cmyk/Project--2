def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return None
    return (celsius * 1.8) + 32