#!/usr/bin/env python3

import sys
import socket
import requests

if len(sys.argv) != 2:
    print("Usage: python3 iplocator.py [host|ip|domain]")
    print("\nEx:  python3 iplocator.py www.google.com")
    print("     python3 iplocator.py 216.58.210.206")
    sys.exit(1)

try:
    ip = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("IP or Host invalid!")
    sys.exit(1)

response = requests.get(f"http://ip-api.com/json/{ip}?fields=33292287")
info = response.json()

print(f"""
Ip Geolocation Tool  

--------------------------------------------------
  [!] IP                       :  {info.get('query')}
  [!] Query Status             :  {info.get('status')}
  [!] Error Message            :  {info.get('message')}
  --------------------------------------------------
  [+] Country/Code             :  {info.get('country')} - {info.get('countryCode')}
  [+] Region/Code              :  {info.get('regionName')} - {info.get('region')}
  [+] City                     :  {info.get('city')}
  [+] Zip                      :  {info.get('zip')}
  [+] District                 :  {info.get('district')}
  [+] Geo                      :  Lat: {info.get('lat')} - Long: {info.get('lon')}
  [+] Paste to Maps            :  {info.get('lat')}, {info.get('lon')}
  [+] Timezone                 :  {info.get('timezone')}
  [+] ISP                      :  {info.get('isp')}
  [+] Organization             :  {info.get('org')}
  [+] AS Number                :  {info.get('as')}
  [+] AS Name                  :  {info.get('asname')}
  [+] Reverse DNS              :  {info.get('reverse')}
  [+] Mobile Connection        :  {info.get('mobile')}
  [+] Proxy/VPN/Tor Exit       :  {info.get('proxy')}
  [+] Hosting/Colo/DataCenter  :  {info.get('hosting')}
  [+] Country Currency         :  {info.get('currency')}
  [+] https://maps.google.com/maps/place/{info.get('lat')}%20{info.get('lon')}
""")
