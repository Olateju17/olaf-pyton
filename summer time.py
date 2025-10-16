def check_clothing_suitability(temperature_celsius):
    if temperature_celsius > 20:
        return "You can wear light clothes."
    else:
        return "It's better to wear warm clothes like a jacket or pullover."


try:
    temp = float(input("Enter the temperature in Celsius: "))
    advice = check_clothing_suitability(temp)
    print(advice)
except ValueError:
    print("Please enter a valid number for temperature.")
