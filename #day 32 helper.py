from helper import generate_password, get_random_joke, print_pattern

print("===== DAY 32 PROJECTS =====")

print("\n--- PASSWORD GENERATOR ---")
length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated Password:", password)

print("\n--- RANDOM JOKE ---")
print(get_random_joke())

print("\n--- NUMBER PATTERN ---")
rows = int(input("Enter number of rows: "))
print_pattern(rows)