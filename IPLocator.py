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
sauce = urllib.request.urlopen('http://ip-api.com/xml/8.8.8.8').read()

#create BeautifulSoup object
soup = bs.BeautifulSoup(sauce, 'xml')

#print the query result without the xml tags
print('[!] IP               :  8.8.8.8')
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
print('[+] https://maps.google.com/maps/place/', soup.status.text)

#Usage: ./iplocator.pl [host] [ip] [domain]
       # perl iplocator.pl [host] [ip] [domain]
#
# Ex:  ./iplocator.pl  www.google.com
#      ./iplocator.pl  216.58.210.206
#
# Usage Limit: The ip-api.com system will automatically ban any IP addresses doing over 150 requests per minute.
#
# If your IP was banned, visit http://ip-api.com/docs/unban
