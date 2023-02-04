import model_add
import model_exp
import model_imp
import view

def main():
    phone_book = {}
    while True:
        print('1. Import from CSV')
        print('2. Export to CSV')
        print('3. Add Contact')
        print('4. View phone book')
        print('5. Quit')
        choice = input('Enter your choice: ')
        if choice == '1':
            filename = input('Enter the filename: ')
            phone_book = model_imp.import_from_csv(filename)
        elif choice == '2':
            filename = input('Enter the filename: ')
            model_exp.export_to_csv(phone_book, filename)
        elif choice == '3':
            name = input('Enter the name: ')
            number = input('Enter the phone number: ')
            model_add.add_contact(phone_book, name, number)
        elif choice == '4':
            view.view_phone_book(phone_book)
        elif choice == '5':
            break
        