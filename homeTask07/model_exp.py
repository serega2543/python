import csv

def export_to_csv(phone_book, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, number in phone_book.items():
            writer.writerows([name, number])