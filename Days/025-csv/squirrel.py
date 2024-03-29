import os

import pandas as pd

root_directory = os.path.dirname(__file__)
data_file = os.path.join(
    root_directory, "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

data = pd.read_csv(data_file)
# print(data.head)

fur_color = data["Primary Fur Color"]

color_count = fur_color.value_counts()

new_data = pd.DataFrame(color_count)
new_data.to_csv("squirrel_count.csv")
