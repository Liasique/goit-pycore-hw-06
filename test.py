from collections import UserDict

#-------Basic classes for the address book system-----
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

# ------- Class for phone number with validation -------
class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

# ------- Class for a contact record containing name and phones -------
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Add a new phone to the list
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        # Replace an old phone number with a new one
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone):
        # Search for a phone by value and return the object
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
# ------- Class for the address book that contains multiple records -------
class AddressBook(UserDict):
    # реалізація класу
	# pass
    def add_record(self, record):
        # Save the contact to the dictionary using name as the key
        self.data[record.name.value] = record

    def find(self, name):
        # Find a contact by name
        return self.data.get(name)

    def delete(self, name):
        # Remove a contact by name
        if name in self.data:
            del self.data[name]

#--------- Decorator to handle user input errors (KeyError, ValueError, IndexError)------
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner
# Split the user input into command and arguments
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# Add new contact with name and phone
@input_error
def add_contact(args, contacts):
     # If not enough arguments, raise error
    if len(args) < 2:
        raise ValueError
    name, phone = args
    # Save name and phone to contacts
    contacts[name] = phone
    return "Contact added."

# Change phone number of existing contact
@input_error
def change_contact(args, contacts):
    if len(args) < 2:
    # If not enough arguments, raise error
        raise ValueError
    name, phone = args
    # Save name and phone to contacts
    contacts[name] = phone
    return "Contact updated."

# Show the phone number of a contact
@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise IndexError
    # Return contact's phone number or message
    name = args[0]
    return contacts.get(name, "Contact not found.")

# Show all contacts and their phone numbers
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    # contacts = {}
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        #if not args and command in ["add", "change", "phone"]:
        if command in ["add", "change"] and len(args) < 2:
            print("Enter the argument for the command")
            continue
        if command == "phone" and len(args) < 1:
            print("Enter the argument for the command")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            # print(add_contact(args, contacts))
            print(add_contact(args, book))
        elif command == "change":
            # print(change_contact(args, contacts))
            print(change_contact(args, book))
        elif command == "phone":
            # print(show_phone(args, contacts))
            print(show_phone(args, book))
        elif command == "all":
            # print(show_all(contacts))
            print(show_all(book))
        else:
            print("Invalid command.")

def test_book():
    print("\n-------- Test -------")
# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

# Run the program
#NB: We don't launch the interactive bot
    # main()

    # Instead we run test to see how address book works
if __name__ == "__main__":
    # main()
    test_book()







# Домашнє завдання до теми "Класи та об'єкти. Робота з даними"
#Спершу виділимо декілька сутностей (моделей)
#У користувача буде адресна книга або книга контактів. Ця книга контактів містить записи. Кожен запис містить деякий набір полів.
#Далі розглянемо вимоги до цих класів та встановимо їх взаємозв'язок, правила, за якими вони будуть взаємодіяти.

#  in Record add:
# 	add_phone(phone)
# 	remove_phone(phone)
# 	•edit_phone(old_phone, new_phone)
# 	•find_phone(phone)

#  in AddressBook add:
# 	add_record(record)
# 	find(name)
# 	delete(name)


#Технiчний опис завдання
"""
Розробіть систему для управління адресною книгою.
"""



#Сутності:
"""
Field: Базовий клас для полів запису.
Name: Клас для зберігання імені контакту. Обов'язкове поле.
Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
AddressBook: Клас для зберігання та управління записами.
"""

#Функціональність:
"""
AddressBook:Додавання записів.
Пошук записів за іменем.
Видалення записів за іменем.
Record:Додавання телефонів.
Видалення телефонів.
Редагування телефонів.
Пошук телефону.
"""

#Рекомендації для виконання

#В якості старту ви можете взяти наступний базовий код для реалізації цього домашнього завдання:

# from collections import UserDict

# class Field:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)

# class Name(Field):
#     # реалізація класу
# 		pass

# class Phone(Field):
#     # реалізація класу
# 		pass

# class Record:
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []

#     # реалізація класу

#     def __str__(self):
#         return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# class AddressBook(UserDict):
#     # реалізація класу
# 		pass



#Після реалізації ваш код має виконуватися наступним чином:

# Створення нової адресної книги
"""   book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
"""


#В наступному домашньому завданні ми додамо цю логіку до нашого бота.


