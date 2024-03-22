import csv
import os

root_directory = os.path.dirname(__file__)
file_path = os.path.join(root_directory, "weather_data.csv")

data: list = []
weather_info: dict = {}


def read_csv(file: str) -> list:
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


def extract_data_to_dict(file: str) -> dict:
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skips the header
        for row in reader:
            day = row[0]
            temperature = int(row[1])  # Converts the string temperature to an integer
            condition = row[2]  # Change 'weather' to 'condition'
            weather_info[day] = {"Temperature": temperature, "Condition": condition}
    return weather_info


def main():
    # data = read_csv(file_path)
    weather_info = extract_data_to_dict(file_path)
    print(weather_info["Monday"]["Temperature"])
    print(weather_info["Monday"]["Condition"])


if __name__ == "__main__":
    main()
