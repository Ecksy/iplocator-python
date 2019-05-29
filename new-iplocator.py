import sys
import requests

header = '''
New IP Locator for Python
------------------------------------'''
print(header)

#get data for API status
request = requests.get('http://ip-api.com/json/8.8.8.8?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,reverse,query')

#get data in JSON form
json_data = requests.get('http://ip-api.com/json/8.8.8.8?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,reverse,query').json()

#check if connectivity is up or down

print(request.status_code)
print(json_data)

if request.status_code == 200:
	print('Query: ' + str(request.status_code) + ' Success, API up!')
#elif request.status_code == 401:
#	print('API key invalid, check account or typo possibly')
#	sys.exit("")
#elif request.status_code == 429:
#	print('Monthly quota reached')
#	sys.exit("")
else:
	print('Query: Oops, API Down! Check connectivity to Hunter.io')
	sys.exit("")

#put account data in to variables
query = json_data['query']
status = json_data['status']
country = json_data['country']
country_code = json_data['countryCode']
region = json_data['region']
region_name = json_data['regionName']
city = json_data['city']
zip_code = json_data['zip']
latitude = json_data['lat']
longitude = json_data['lon']
time_zone = json_data['timezone']
isp_provider = json_data['isp']
organization = json_data['org']
as_number = json_data['as']
reverse_dns = json_data['reverse']
district_name = json_data['district']

#print data
print("")
print('Query:' + query)
print(status)
print(country)
print(country_code)
print(region)
print(region_name)
print(city)
print(zip_code)
print(latitude)
print(longitude)
print(time_zone)
print(isp_provider)
print(organization)
print(as_number)
print(reverse_dns)
print(district_name)
sys.exit()
