import bs4 as bs
import urllib.request

#print header out: ''' prints multiple lines
header = '''
Ip Geolocation Tool
By: Ecksy
------------------------------------'''
print(header)

#read IP address(s) from input or file
#ip = "argument from input"

#get ip-api url
#sauce = urllib.request.urlopen('http://ip-api.com/xml/'ip).read()
# sauce = urllib.request.urlopen('http://ip-api.com/xml/69.222.199.70').read()
sauce = urllib.request.urlopen('http://ip-api.com/xml/'+ip_address).read()

#create BeautifulSoup object
soup = bs.BeautifulSoup(sauce, 'xml')

#print the query result without the xml tags
print('[!] IP               : ', soup.query.query.text)
print('[!] Query Status     : ', soup.status.text)
print('[!] Error Message    : ', soup.message)
print('------------------------------------')
print('[+] Country/Code     : ', soup.country.text, '-', soup.countryCode.text)
print('[+] Region/Code      : ', soup.regionName.text, '-', soup.region.text)
print('[+] City             : ', soup.city.text)
print('[+] Zip              : ', soup.zip.text)
print('[+] Geo              :  Lat:', soup.lat.text, '- Long:', soup.lon.text)
print('[+] Paste to Maps    : ', soup.lat.text, ', ', soup.lon.text)
print('[+] Timezone         : ', soup.timezone.text)
print('[+] ISP              : ', soup.isp.text)
print('[+] Organization     : ', soup.org.text)
# print('[+] AS Number/Name   : ', soup.as.text)
print('[+] AS Number/Name   : ', soup.find_all('as'))
print('[+] https://maps.google.com/maps/place/', soup.status.text)

#Usage: ./iplocator.py [host] [ip] [domain]
       # python iplocator.py [host] [ip] [domain]
#
# Ex:  ./iplocator.py  www.google.com
#      ./iplocator.py  216.58.210.206
#
# Usage Limit: The ip-api.com system will automatically ban any IP addresses doing over 150 requests per minute.
#
# If your IP was banned, visit http://ip-api.com/docs/unban

# Test snippet
# def Geolocate(IP):
#     URL = "http://ip-api.com/json/"+str(IP)
#     data = str(os.open("curl -s "+URL).read())
#     obj = json.loads(data)
#     for item in obj:
#         print(str(item)+" : "+str(obj[item]))

#pick target/s
# parser.add_argument('-m', '--my-ip',
#                     dest='myip',
#                     action='store_true',
#                     help='Get Geolocation info for my IP address.')
#
# parser.add_argument('-t', '--target',
#                     help='IP Address or Domain to be analyzed.')
#
# parser.add_argument('-T', '--tlist',
#                     metavar='file',
#                     type=checkFileRead,
#                     help='A list of IPs/Domains targets, each target in new line.')
