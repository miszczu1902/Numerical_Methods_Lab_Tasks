import csv


def read_from_csv():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        items = list(reader)
        size = len(items)

        if size >= 11:
            return "Maksymalna ilosc niewiadomych to 10!"

    return items, size
