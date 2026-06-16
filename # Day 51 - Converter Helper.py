# Day 51 - Converter Helper

def quick_demo():
    print("Quick demo:")
    print("0°C → F:", celsius_to_fahrenheit(0))
    print("32°F → C:", fahrenheit_to_celsius(32))
    print("1m → ft:", meters_to_feet(1))
    print("3.28084ft → m:", feet_to_meters(3.28084))

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def meters_to_feet(m):
    return m * 3.28084

def feet_to_meters(ft):
    return ft / 3.28084

if __name__ == "__main__":
    quick_demo()