import os
from dotenv import load_dotenv
import requests

API_KEY = os.getenv("API_KEY")


while True:
    nation = input("Enter the name of country or stop to finish the process: ")
    if nation.lower() == "stop":
        break

    data = requests.get(f"https://api.countrylayer.com/v2/name/{nation}?access_key={API_KEY}&fulltext=true").json()
    print(data)
    country = data[0]
    name = country["name"]
    capital = country["capital"]
    country_kod = country['alpha2Code']
    callingCodes = country["callingCodes"]
    other_names = country["altSpellings"]
    region = country["region"]
    print(f"Country name: {name}, "
          f"\nCapital: {capital}, "
          f"\nCountry code: {country_kod}, "
          f"\nPhone number code: {callingCodes}, "
          f"\nAlternative names: {other_names}, "
          f"\nRegion: {region}.")