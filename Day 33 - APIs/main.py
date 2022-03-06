import smtplib
import requests
import datetime
import pytz


MY_LAT = 11.934675
MY_LNG = 79.800493

my_email = "your_email@gmail.com"
password = "your_password"


def iss_close():
    response1 = requests.get(url='http://api.open-notify.org/iss-now.json')

    response1.raise_for_status()
    data1 = response1.json()

    lat = float(data1["iss_position"]["latitude"])
    lng = float(data1["iss_position"]["longitude"])
    if(lat >= MY_LAT-5 and lat <= MY_LAT+5 and lng >= MY_LNG-5 and lng <= MY_LNG+5):
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


def is_night():
    response2 = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters)
    response2.raise_for_status()
    data = response2.json()
    sunrise = int({data["results"]["sunrise"].split("T")[1].split(":")[0]})
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    nows = datetime.datetime.now()
    now = nows.astimezone(pytz.utc)
    if(now.hour >= sunset or now.hour <= sunrise):
        return True


if iss_close() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="tbot16022@gmail.com", msg=f"Subject: ISS Above!\n\nLook Up!")
    connection.close()
