from collections import UserDict
from datetime import datetime, date, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError("Номер має складатися з 10 цифр")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d-%m-%Y").date()      
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break
  
    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number
                break

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data [record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
    def find_next_weekday(self, start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    def adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5:  
            return self.find_next_weekday(birthday, 0)  
        return birthday

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                if 0 <= (birthday_this_year - today).days <= days:
                    congratulation_date = self.adjust_for_weekend(birthday_this_year)
                    congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": congratulation_date_str
                    })

        return upcoming_birthdays

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func) -> str:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Incorrect value."
        except IndexError:
            return "Give me name and phone please."
        except KeyError:
            return "Name not found."

    return inner

@input_error
def add_contact(args, book: AddressBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)
    if record and record.find_phone(old_phone):
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        raise KeyError("Contact or phone not found.")

@input_error
def show_phone(args, book: AddressBook) -> list:
    name = "".join(args)
    record = book.find(name)
    if record:
        phones = '; '.join(p.value for p in record.phones) if record.phones else 'No phones'
        return phones
    else:
        raise KeyError("Contact not found.")

@input_error
def show_all(book: AddressBook) -> list:
    return book

@input_error
def add_birthday(args, book: AddressBook) -> str:
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError("Contact not found.")

@input_error
def show_birthday(args, book: AddressBook) -> str:
    name = "".join(args)
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday.value.strftime("%d-%m-%Y")
        else:
            return "No birthday for this contact."
    else:
        raise KeyError("Contact not found.")

@input_error
def birthdays(args, book: AddressBook) -> str:
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        result = "\n".join(f"{item['name']} - {item['birthday']}" for item in upcoming_birthdays)
    else:
        result = "No upcoming birthdays."
    return result


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()