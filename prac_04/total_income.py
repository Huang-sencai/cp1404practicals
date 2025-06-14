"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))
    for int_list_months in range(1,months+1):
        income = float(input(f"Enter income for month {int_list_months}:"))
        incomes.append(income)
    print("\nIncome Report\n-------------")
    total = 0
    for int_list_months in range(1,months+1):
        income = incomes[int_list_months-1]
        total += income
        print(f"Month {int_list_months:2} - Income: ${income:10.2f} Total: ${total:10.2f}")
main()
