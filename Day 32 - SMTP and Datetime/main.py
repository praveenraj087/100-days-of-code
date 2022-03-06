import datetime as dt
import smtplib
import pandas
import random

my_email = "your_email@gmail.com"
password = "your_password"


now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
data = pandas.read_csv("birthdays.csv")

bday_dict = {(data_row["month"], data_row["day"])             : data_row for (index, data_row) in data.iterrows()}


if today in bday_dict:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        contents = letter.read()
        new_letter = contents.replace("[NAME]", bday_dict[today]["name"])
        connection.sendmail(from_addr=my_email,
                            to_addrs="tbot16022@gmail.com", msg=f"Subject: Happy Birthday!\n\n{new_letter}")
        connection.close()
