import csv

def import_from_csv(filename):
    phone_book = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            phone_book[row[0]] = row[1]
    return phone_book