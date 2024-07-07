from pathlib import Path

def get_cats_info(path: Path) -> list:
    path = Path(path)
    keys = ["id", "name", "age"]
    database = []

    try:
        with open(path, "r", encoding="utf-8", errors="strict") as file:
            lst = [el.strip().split(",") for el in file.readlines()]
            database = [dict(zip(keys, el)) for el in lst]

    except FileNotFoundError:
        print("File not found")
    except UnicodeEncodeError:
        print("Incorrect text encoding")
    
    return database

print(get_cats_info(input("Path: ")))