import csv

def read_wimbledon_data(filename):
    """Read Wimbledon CSV file and return list of records."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            records.append(row)
    return records

def count_champions(records):
    """Count the number of wins for each champion."""
    champion_wins = {}
    for record in records:
        champion = record[2]  # Champion's name is in the 3rd column
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
    return champion_wins

def get_unique_countries(records):
    """Get a set of unique countries from the champions."""
    countries = {record[1] for record in records}  # Champion's country is in the 2nd column
    return sorted(countries)

def display_champions(champion_wins):
    """Display champions and their number of wins."""
    print("Wimbledon Champions:")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")

def display_countries(countries):
    """Display unique countries in alphabetical order."""
    print("\nThese countries have won Wimbledon:")
    print(", ".join(countries))

def main():
    filename = "wimbledon.csv"
    records = read_wimbledon_data(filename)

    champion_wins = count_champions(records)
    countries = get_unique_countries(records)

    display_champions(champion_wins)
    display_countries(countries)

if __name__ == "__main__":
    main()