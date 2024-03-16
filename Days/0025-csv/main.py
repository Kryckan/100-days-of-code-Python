import csv
import os

root_directory = os.path.dirname(__file__)
file_path = os.path.join(root_directory, "weather_data.csv")

data: list = []


def read_csv(file: str) -> list:
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


def main():
    data = read_csv(file_path)
    print(data)


if __name__ == "__main__":
    main()
