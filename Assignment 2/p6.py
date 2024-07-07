import pandas as pd
import requests
import time


def fetch_iss_location():
    url="http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    if response.status_code == 200:
        iss_data = response.json()
        timestamp = iss_data['timestamp']
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']
        return timestamp, latitude, longitude
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None



def collect_and_write_data(min_records=100):
    data = []

    while len(data) < min_records:
        location = fetch_iss_location()
        if location:
            data.append(location)
            print(f"Collected record {len(data)}/{min_records}")
        time.sleep(5)  

   
    df = pd.DataFrame(data, columns=['timestamp', 'latitude', 'longitude'])


    csv_filename = 'data.csv'
    df.to_csv(csv_filename, index=False)
    print(f"CSV file '{csv_filename}' created with {min_records} records.")


if __name__ == '__main__':
    collect_and_write_data(min_records=100)

