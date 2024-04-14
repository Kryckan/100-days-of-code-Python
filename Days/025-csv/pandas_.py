import os

import pandas as pd

root_directory = os.path.dirname(__file__)
file_path = os.path.join(root_directory, "weather_data.csv")

data = pd.read_csv(file_path)


print(data)

# average_temp = data["temp"].mean()
# print("Average temp:", data["temp"].mean())
# print("Max temp: ", data["temp"].max())
# print("Min temp: ", data["temp"].min())

# print(data[data.temp == data.temp.max()])

# monday_data = data[data.day == "Monday"]

# print(monday_data.temp)
# monday_temp_f = (monday_data.temp * 9 / 5) + 32
# print("Monday's temperature in Fahrenheit:", monday_temp_f)
