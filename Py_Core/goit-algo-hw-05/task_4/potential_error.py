def input_error(func: function) -> str:
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