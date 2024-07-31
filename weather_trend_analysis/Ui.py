from api import retrieve_weather_details,get_temperature_stats,get_direction

print("Give desired Year :",end=' ')
year = int(input()) 
print("Give desired Month :",end=' ')
month = int(input())  


# Retrieve weather details
weather_details = retrieve_weather_details(year=year, month=month)
print("Weather Details:")
print(weather_details)


# Get temperature statistics
temp_stats = get_temperature_stats(year=year)
print("\nTemperature Statistics:")
print(temp_stats)

print("\n Common direction")
direction=get_direction()
print(direction200309)