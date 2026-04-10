#Day 6 - List Helper
def add_item(items, item):
    items.append(item)
    return items

shopping = ["milk"]
add_item(shopping, "bread")
print("Shopping:", shopping)