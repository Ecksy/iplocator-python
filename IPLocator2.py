#!/usr/bin/env python3
import sys
import socket
import requests

def print_help():
    print("""
Usage:
  python3 iplocator.py [host|ip|domain]
  python3 iplocator.py -i [input_file]

Examples:
  python3 iplocator.py www.google.com
  python3 iplocator.py 216.58.210.206
  python3 iplocator.py -i input.txt
""")

def get_geolocation(target):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"IP or Host invalid: {target}")
        return

    response = requests.get(f"http://ip-api.com/json/{ip}?fields=33292287")
    info = response.json()

    print(f"""
--------------------------------------------------
Target: {target}
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

if len(sys.argv) < 2:
    print_help()
    sys.exit(1)

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print_help()
    sys.exit(0)

if sys.argv[1] == '-i':
    if len(sys.argv) != 3:
        print("Invalid number of arguments for -i option")
        sys.exit(1)
    
    input_file = sys.argv[2]
    try:
        with open(input_file, 'r') as f:
            for line in f:
                get_geolocation(line.strip())
    except FileNotFoundError:
        print(f"No such file: {input_file}")
else:
    get_geolocation(sys.argv[1])
