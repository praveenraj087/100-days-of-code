import smtplib
import datetime as dt
import random
my_email = "your_email@gmail.com"
password = "your_password"


nows = dt.datetime.now()
days = nows.day
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

with open("quotes.txt") as quotes_file:
    contents = quotes_file.readlines()
    if(days == 0):
        connection.sendmail(from_addr=my_email,
                            to_addrs="tbot16022@gmail.com", msg=f"Subject: Quote of the Day\n\n{random.choice(contents)}")
        connection.close()
    else:
        print("It's not Monday")
