# Day 43 - JSON Helper
import json

def show_keys():
    print("All keys in day43_data.json:")
    with open("day43_data.json", "r") as f:
        data = json.load(f)
    print(", ".join(data.keys()))

def add_skill(skill):
    with open("day43_data.json", "r") as f:
        data = json.load(f)
    data["skills"].append(skill)
    with open("day43_data.json", "w", indent=2) as f:
        json.dump(data, f)
    print("Skill added:", skill)

if __name__ == "__main__":
    show_keys()
    add_skill("SQL")