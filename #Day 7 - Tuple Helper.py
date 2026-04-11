#Day 7 - Tuple Helper
def get_name_age(data):
    return data[0], data[1]

info = ("Ram", 25)
name, age = get_name_age(info)
print(f"{name} is {age}")