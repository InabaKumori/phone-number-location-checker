import phonenumbers
from phonenumbers import geocoder

def normalize_phone_number(phone_number):
    # Remove any non-digit characters from the phone number
    normalized_number = ''.join(filter(str.isdigit, phone_number))
    
    # Add the country code if missing (assuming US numbers)
    if len(normalized_number) == 10:
        normalized_number = '+1' + normalized_number
    
    return normalized_number

def get_location(phone_number):
    # Normalize the phone number
    normalized_number = normalize_phone_number(phone_number)
    
    # Parse the phone number
    parsed_number = phonenumbers.parse(normalized_number, None)
    
    # Get the location information
    location = geocoder.description_for_number(parsed_number, "en")
    
    return location

# Example usage
phone_number = input("Enter a phone number: ")
location = get_location(phone_number)
print(f"Location: {location}")
