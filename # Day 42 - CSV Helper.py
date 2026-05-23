# Day 42 - CSV Helper
import csv

def show_as_table():
    print("Data as table:")
    with open("day42_data.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        print(" | ".join(header))
        print("-" * 30)
        for row in reader:
            print(" | ".join(row))

if __name__ == "__main__":
    show_as_table()