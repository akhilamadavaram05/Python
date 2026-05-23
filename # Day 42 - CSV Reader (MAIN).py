# Day 42 - CSV Reader (MAIN)
import csv

def main():
    # Create sample CSV
    data = [
        ["Name", "Age", "City"],
        ["Akhila", "25", "Hyderabad"],
        ["Sai", "26", "Bengaluru"],
        ["Ravi", "27", "Chennai"]
    ]
    with open("day42_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    # Read CSV
    print("CSV data:")
    with open("day42_data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

if __name__ == "__main__":
    main()