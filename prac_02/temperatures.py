"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def calculate_fahrenheit():
     return celsius * 9.0 / 5 + 32
def calculate_celsius():
    return  5 / 9 * (fahrenheit - 32)

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = calculate_fahrenheit()
        print(f"Result:{fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit:"))
        celsius = calculate_celsius()
        print(f"Result:{celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")