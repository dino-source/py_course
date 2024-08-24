temperature = int(input("Enter a temperature: "))

forecast = input("Enter a forecast: ")

if not forecast == "rain" and (temperature > 60 and temperature < 80):
    print("Go outside!")
else:
    print("Stay inside!")

print("Because temperature", temperature, "and forecast", forecast)
