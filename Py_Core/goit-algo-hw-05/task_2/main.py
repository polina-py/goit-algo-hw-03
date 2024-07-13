import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r"\-?\d+(?:\.\d*)?"
    numbers = re.findall(pattern, text)
    for num in numbers:
        yield float(num)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    total_income = sum(func(text))
    return total_income

text = "Word 12 0 Second Word 45 -3 5.7 ?"
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")