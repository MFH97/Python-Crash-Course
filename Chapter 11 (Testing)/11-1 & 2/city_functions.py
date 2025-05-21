# city_functions.py

def get_cities_name(city_name, country_name, population=None):
    # Capitalize the first letter of each word
    full_name = f"{city_name.title()}, {country_name.title()}"
    
    # If population is provided, include it in the string with proper spacing
    if population is not None:
        full_name += f" – population {population}"
    else:
        full_name = f"{city_name.title()}, {country_name.title()}"
        
    return full_name.strip()  # Ensure no extra spaces are included
