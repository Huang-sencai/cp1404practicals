def main():
    number()
    checker()
def number():
    list_numbers = []
    for i in range(5):
        num = int(input("Number: "))
        list_numbers.append(num)
    print(f"The first number is {list_numbers[0]}")
    print(f"The last number is {list_numbers[-1]}")
    print(f"The smallest number is {min(list_numbers)}")
    print(f"The largest number is {max(list_numbers)}")
    average = sum(list_numbers) / len(list_numbers)
    print(f"The average of the numbers is {average}")

def checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")



main()
