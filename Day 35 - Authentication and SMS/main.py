import requests
from twilio.rest import Client

api_key = "your_api_Key"

MY_LAT = -32.960288
MY_LNG = -60.659226

account_sid = "your_account_sid"
auth_token = "your_auth_token"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "minutely,daily,current",
    "appid": api_key,
}
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
res = response.json()
weather_list = []
rain = False
weather_id = res["hourly"][0]["weather"][0]["id"]
for i in range(0, 13):
    weather_list.append(res["hourly"][i]["weather"][0]["id"])
for n in weather_list:
    if n < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="it's going to rain today! Better Bring an Umbrella With you",
                        from_='from_number',
                        to='to_number'
                    )
    print(message.status)
