def add_contact(args, contacts) -> str:
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Enter name and phone number."

def change_contact(args, contacts) -> str:
    try:
        name, phone = args
        if name in contacts.keys():
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Name not found."
    except ValueError:
        return "Enter name and phone number."

def show_phone(args, contacts) -> list:
    try:
        name = "".join(args)
        if name in contacts.keys():
            return contacts[name]
        else:
            return "Phone number not found."
    except ValueError:
        return "Enter name."


def show_all(contacts) -> list:
    return contacts

