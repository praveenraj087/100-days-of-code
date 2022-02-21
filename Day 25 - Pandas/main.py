import csv
from numpy import average
import pandas

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(row[1])
#     print(temp)


data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
avrg = average(temp_list)
print(avrg)
max_temp = data["temp"].max()
print(max_temp)

print(data[data["temp"] == max_temp])
monday = data[data.day == "Monday"]
temp_in_f = (monday.temp*1.8)+32
print(temp_in_f)
