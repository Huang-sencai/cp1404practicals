def main():
    score = get_valid_score()
    choice = ""
    while choice.upper() != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid choice.")

def print_menu():
    print("Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
            score = int(input("Enter a score (0-100): "))
            while score < 0 or score > 100:
                    print("Invalid score.")
                    score = int(input("Enter a score (0-100): "))
            return score

def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * score)


main()