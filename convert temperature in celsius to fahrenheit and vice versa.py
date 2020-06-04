# Python Program to convert temperature in celsius to fahrenheit...
celsius = float(input("Enter Number in celsius :"))
fahrenheit = (celsius * 1.8) + 32   #formula
print("%0.1f celsius is equal to %0.1f fahrenheit"%(celsius,fahrenheit))

#fahrenheit to celsius...
fahrenheit = float(input("Enter NUmber in fahrenheit :"))
celsius = (fahrenheit - 32) * 0.5   #formula
print("%0.1f fahrenheit is equal to %0.1f celsius"%(fahrenheit,celsius))
