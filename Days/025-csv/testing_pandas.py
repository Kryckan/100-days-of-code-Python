import os

import pandas as pd
import polars as pl

root_directory = os.path.dirname(__file__)
file_path = os.path.join(root_directory, "weather_data.csv")

data = pd.read_csv(file_path)

data2 = pl.read_csv(file_path)

average_temp = data2["temp"].mean()
print("Average temp:", average_temp)
