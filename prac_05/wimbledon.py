FILENAME="wimbledon.csv"
def main():
    data=read_data()
    champion,counties=winner_data(data)
    display(champion,counties)
def read_data():
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        data = [line.strip().split(',') for line in in_file]
        in_file.close()
    return data
def winner_data(data):
    champion_to_count = {}
    countries_set = set()
    for row in data:
        champion = row[2]
        country = row[1]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
        countries_set.add(country)
    return champion_to_count, countries_set
def display(champion_to_count, countries_set):
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print()
    countries_string = ", ".join(sorted(countries_set))
    print(f"These {len(countries_set)} countries have won Wimbledon:")
    print(countries_string)