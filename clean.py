import json
import pandas as pd


def clean_data_into_csv():
    try:
        with open("raw_earthquakes.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            print(
                f"{data['metadata']['count']} earthquakes retrieved successfully !")

            cleaned_list = []
            for i in data['features']:
                temp_dict = {
                    'time': i['properties']['time'],
                    'place': i['properties']['place'],
                    'magnitude': i['properties']['mag'],
                    'longitude': i['geometry']['coordinates'][0],
                    'latitude': i['geometry']['coordinates'][1],
                    'depth': i['geometry']['coordinates'][2]
                }

                cleaned_list.append(temp_dict)

            df = pd.DataFrame(cleaned_list)
            df['time'] = pd.to_datetime(df['time'], unit='ms')
            count = df.isnull().sum()
            if count.sum() == 0:
                print("\nNo null values found in any column.")
            else:
                print("\nNull count is: ", count)
            df.index += 1
            df.to_csv('clean_earthquakes.csv', index_label='id')
            print("\nThe data has been cleaned and loaded into csv.")

    except FileNotFoundError:
        print("Error: The file raw_earthquakes.json was not found. ")
