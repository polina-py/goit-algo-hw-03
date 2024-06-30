#Task 2

import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    lottery_numbers = []
    if min >= 1 and max <= 1000 and min <= quantity <= max:
        while len(lottery_numbers) < quantity:
            num = random.randint(min, max)
            if num not in lottery_numbers:
                lottery_numbers.append(num)
            else:
                continue 
    
        lottery_numbers.sort()
        return lottery_numbers
    else:
        return lottery_numbers

print(f"Ваші лотерейні числа: {get_numbers_ticket(1, 1000, 20)}")