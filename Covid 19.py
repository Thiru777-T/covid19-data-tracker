import requests
import pandas as pd

# Fetch data for all countries
url = "https://disease.sh/v3/covid-19/countries"

response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.json_normalize(data)

# Select useful columns
df = df[['country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 
         'recovered', 'active', 'critical', 'casesPerOneMillion']]

# Save to CSV File
df.to_csv("covid_data.csv", index=False)

print("✅ Live COVID-19 data collected and saved.")

import schedule
import time

def collect_data():
    # (Insert the fetch code above here)
    print("Data updated!")

schedule.every().day.at("10:00").do(collect_data)

while True:
    schedule.run_pending()
    time.sleep(60)
