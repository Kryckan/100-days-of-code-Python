from datetime import datetime
import pandas as pd
import requests
from iss_pos import ISSPosition
import pytz

MY_LAT = 59.539579
MY_LNG = 17.9101604
my_lat_max = MY_LAT + 5
my_lat_min = MY_LAT - 5
my_lng_max = MY_LNG + 5
my_lng_min = MY_LNG - 5

API_URL = "https://api.sunrise-sunset.org/json"
iss_position = ISSPosition()

params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}


def get_sun_data():
    response = requests.get(
        url=API_URL,
        params=params,
    )
    response.raise_for_status()
    if not response.status_code == 200:
        raise Exception("Request failed")
    else:
        return response.json()


# Convert response to dataframe
sun_data_ = pd.DataFrame(get_sun_data())


def format_time(iso_time):
    return (datetime.fromisoformat(iso_time) + pd.Timedelta(hours=1)).strftime(
        "%H:%M:%S"
    )


sunrise = format_time(sun_data_["results"]["sunrise"])
sunset = format_time(sun_data_["results"]["sunset"])
sun_noon = format_time(sun_data_["results"]["solar_noon"])

# print(f"Sunrise: {sunrise}, Sunset: {sunset}, Sun Noon: {sun_noon}")


def check_visibility():
    iss_pos = iss_position.get_iss_position()
    iss_data = pd.DataFrame(iss_pos)

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    sunset_time = datetime.fromisoformat(sun_data_["results"]["sunset"]).replace(
        tzinfo=None
    )
    sunrise_time = datetime.fromisoformat(sun_data_["results"]["sunrise"]).replace(
        tzinfo=None
    )

    if my_lat_min <= iss_lat <= my_lat_max and my_lng_min <= iss_lng <= my_lng_max:
        if datetime.now() > sunset_time or datetime.now() < sunrise_time:
            print("ISS is overhead and can be seen! Take a look!")
        else:
            print("ISS is overhead but cannot be seen")
    else:
        print("ISS is not overhead")


check_visibility()
