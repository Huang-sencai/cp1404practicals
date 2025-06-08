name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")
with open("number.txt", "r") as numbers_file:
    number1 = int(numbers_file.readline())
    number2 = int(numbers_file.readline())
    print(number1 + number2)

total_number = 0
with open("number.txt", "r") as numbers_file:
    for line in numbers_file:
        total_number += int(line)
print(total_number)