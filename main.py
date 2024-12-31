import requests
import socks
import socket
from geopy.geocoders import Nominatim

# Function to get public IP address and location
def get_ip_and_location():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        response.raise_for_status()
        ip = response.json().get("ip")
        
        # Get location using IP
        location_response = requests.get(f"https://ipapi.co/{ip}/json/")
        location_response.raise_for_status()
        location = location_response.json()
        
        print(f"Public IP Address: {ip}")
        print(f"Location: {location.get('city')}, {location.get('region')}, {location.get('country_name')}")
    except requests.RequestException as e:
        print(f"Failed to get IP and location: {e}")

# Function to configure SOCKS proxy using PySocks
def set_socks_proxy(proxy_address, proxy_port):
    socks.set_default_proxy(socks.SOCKS5, proxy_address, proxy_port)
    socket.socket = socks.socksocket  # Route all traffic through the proxy

# Main script
if __name__ == "__main__":
    # Step 1: Get current IP and location
    print("Getting current IP and location...")
    get_ip_and_location()

    # Step 2: Configure proxy
    proxy_ip = "proxy_address"  # Replace with your proxy IP
    proxy_port = 1080  # Replace with your proxy port
    print("\nSetting SOCKS5 proxy...")
    set_socks_proxy(proxy_ip, proxy_port)

    # Step 3: Get proxy IP and location
    print("Getting proxy IP and location...")
    get_ip_and_location()
