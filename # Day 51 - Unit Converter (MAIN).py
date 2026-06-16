# Day 51 - Unit Converter (MAIN)

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def meters_to_feet(m):
    return m * 3.28084

def feet_to_meters(ft):
    return ft / 3.28084

def main():
    print("Unit Converter")
    while True:
        print("\n1. C → F  2. F → C  3. m → ft  4. ft → m  5. Quit")
        choice = input("Choice: ")
        if choice == "5":
            break

        try:
            val = float(input("Value: "))
        except ValueError:
            print("Invalid number")
            continue

        if choice == "1":
            print("Result:", celsius_to_fahrenheit(val))
        elif choice == "2":
            print("Result:", fahrenheit_to_celsius(val))
        elif choice == "3":
            print("Result:", meters_to_feet(val))
        elif choice == "4":
            print("Result:", feet_to_meters(val))
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()