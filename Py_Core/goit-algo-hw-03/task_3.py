#Task 3

import re

phone_number = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
    ]

contact_list = []

def normalize_phone(phone_number: list) -> list:
    for i in phone_number:
        i = re.sub(r"[^+\d]", "", i)
        if not i.startswith("+380"):
            if i.startswith("38"):
                i = "+" + i
                contact_list.append(i)
            else: 
                i = "+38" + i
                contact_list.append(i)
        else:
            contact_list.append(i)
    
    return contact_list

print(f"Нормалізовані номери телефону: {normalize_phone(phone_number)}")