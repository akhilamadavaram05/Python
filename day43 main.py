# Day 43 - JSON Reader / Writer (MAIN)
import json

def main():
    # Write sample JSON
    data = {
        "name": "Akhila",
        "age": 25,
        "city": "Hyderabad",
        "skills": ["Python", "Git"]
    }
    with open("day43_data.json", "w", indent=2) as f:
        json.dump(data, f)
    print("Written data.json")

    # Read JSON
    print("Read data:")
    with open("day43_data.json", "r") as f:
        loaded = json.load(f)
    print(json.dumps(loaded, indent=2))

if __name__ == "__main__":
    main()