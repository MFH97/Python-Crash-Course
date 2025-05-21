from city_functions import get_cities_name
#city.py

print('Enter "q" at any time to quit.')

while True:
  city_name = input("\nEnter city name: ")
  if city_name == 'q':
    break
  country_name = input("Enter country name: ")
  if country_name == 'q':
    break
  population = input("Enter population: ")
  if population == 'q':
    break

  city = get_cities_name(city_name, country_name, population)
  print("\nCITY DETAILS: " + city + '.')