import random
def main():
    numbers_quick_picks = int(input("How many quick picks? "))
    for i in range(numbers_quick_picks):
        numbers = generate_quick_pick()
        for j in numbers:
            print(f"{j:>2} ",end="")
        print()
def generate_quick_pick():
    picked_numbers = []
    while len(picked_numbers) < 6:
        num = random.randint(1,45)
        if num not in picked_numbers:
            picked_numbers.append(num)
    picked_numbers.sort()
    return picked_numbers
main()