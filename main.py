import requests
from datetime import datetime
import time
# Put your latitude and longitude.
MY_LAT = 51.507351
MY_LONG = -0.127758

# ------------------------------------------------

def is_iss_overhead():

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

# ------------------------------------------------

def is_night():

    # Set your parameters in a dictionary.
    # The keys in the dictionary are the parameters specified in the API documentation.
    # Add dictionary with parameters to the get request.
    parameters= {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # Split method: splits a string using a separator into a list.
    # Split the item further apart with index 1.

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# ------------------------------------------------

while True:
    #So this while loop will run endless, but we can tell it to sleep for 60 seconds.
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("It worked baby! The ISS is over you :)")
