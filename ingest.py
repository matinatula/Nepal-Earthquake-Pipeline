import requests
import json
import pprint

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

params = {'format': 'geojson', 'starttime': '2015-01-01', 'endtime': '2024-12-31', 'minlatitude': '26.347',
          'maxlatitude': '30.447', 'minlongitude': '80.058', 'maxlongitude': '88.201', 'minmagnitude': '2.5'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = json.loads(response.text)  # data -> python dictionary
    print(
        f"Saved {data['metadata']['count']} earthquakes to raw_earthquakes.json ")

    json_str = json.dumps(data, indent=4)
    with open("raw_earthquakes.json", "w") as f:
        f.write(json_str)
else:
    print(f"Error: {response.status_code}")
