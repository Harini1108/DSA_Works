#Asking user for temperature in Celsius
temp_celcius = float(input("Enter the temperature in celcius:"))

#Converting to fahrenheit
temp_fahrenheit = ( temp_celcius * 9/5 ) + 32
print("Temperature in Fahrenheit:",temp_fahrenheit)

#printing advice
if temp_celcius < 0:
 print("Very cold! Wear thick jacket")

elif 0 <= temp_celcius >= 15:
 print("Cold. Wear jacket")

elif 16 <= temp_celcius >= 25:
 print("Nice weather")

else:
 print("Hot! Stay hydrated")
  