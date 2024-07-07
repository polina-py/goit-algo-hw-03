from pathlib import Path
import statistics

def unpack(lst:list) -> list:
    salary = [int(el[1]) for el in lst]
    return salary

def total_salary(path: Path) -> float:
    path = Path(path)
    total_salary = 0
    mean_salary = 0

    try:
        with open(path, "r", encoding="utf-8", errors="strict") as info:
            lst = [el.strip().split(",") for el in info.readlines()]
            clean_list = unpack(lst)
            total_salary = sum(clean_list)
            mean_salary = statistics.mean(clean_list)
    except FileNotFoundError:
        print("File not found")
    except UnicodeEncodeError:
        print("Incorrect text encoding")
    
    return f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {mean_salary}"

print(total_salary(input("Path: ")))