import os

import pandas as pd

root_directory = os.path.dirname(__file__)
file_path = os.path.join(root_directory, "weather_data.csv")

data = pd.read_csv(file_path)
print(data)
