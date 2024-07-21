from potential_error import input_error

@input_error
def add_contact(args, contacts) -> str:
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts) -> str:
    if len(args) != 2:
        raise IndexError
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts) -> list:
    name = "".join(args)
    if name in contacts.keys():
        return contacts[name]
    else:
        raise KeyError

@input_error
def show_all(contacts) -> list:
    return contacts

