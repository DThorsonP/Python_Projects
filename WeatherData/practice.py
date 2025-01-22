#! /Users/david.thorson/.local/pipx/venvs/pandas/bin/python

import csv
import pandas as pd
import numpy as np

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pd.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))

temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
# print(round(data["temp"].mean(), 2))
# print(data["temp"].max())

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

