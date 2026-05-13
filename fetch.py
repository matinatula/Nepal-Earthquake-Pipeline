import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

params = {'format': 'geojson','starttime': '2015-01-01', 'endtime': '2015-01-31', 'minlatitude':'26.347', 'maxlatitude':'30.447','minlongitude':'80.058','maxlongitude':'88.201','minmagnitude':'2.5'}

response = requests.get(url,params=params)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")

