import requests
from geopy.geocoders import Nominatim

# Function to get public IP address and locaiton

def get_ip_and_location():
  try:
      response = requests.get("https://api64.ipify.org?format=json")
      response.raise_for_status()
      ip = response.json().get("ip")

      # Get location using IP
      location_response = requests.get(f"https://ipapi.co/{ip}/json/")
      location_response.raise_for_status()
      location = location_response.json()

      print(f"Public IP Address : {ip}")
      print(f"Location {location.get('city')}, {location.get('region')}, {location.get('country_name')}")
  except requests.RequestException as e:
      print(f"Failed to get IP and Location")



# Main Script
if __name__== "__main__":
   #Step 1 : Get Current IP and Location
   print ("Getting current IP and Location")
   get_ip_and_location()


