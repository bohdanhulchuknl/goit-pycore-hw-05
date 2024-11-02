def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid input. Please provide the correct arguments."
    return inner

contacts = {}

@input_error
def add_contact(args):
    """
    Додає контакт до словника контактів.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    """
    Повертає номер телефону для заданого імені.
    """
    name = args[0]
    return contacts[name]

@input_error
def show_all(args):
    """
    Повертає всі контакти у вигляді рядка.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def show_help(args):
    """
    Повертає список доступних команд.
    """
    return (
        "Доступні команди:\n"
        "add - Додати контакт. Формат: add <ім'я> <телефон>\n"
        "phone - Отримати номер телефону за іменем. Формат: phone <ім'я>\n"
        "all - Показати всі контакти\n"
        "help - Показати список доступних команд\n"
        "exit - Вийти з програми"
    )

def main():
    print(show_help([])) 
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "add":
            args = input("Enter the argument for the command: ").strip().split()
            print(add_contact(args))
        elif command == "phone":
            args = input("Enter the argument for the command: ").strip().split()
            print(get_phone(args))
        elif command == "all":
            print(show_all([]))
        elif command == "help":
            print(show_help([]))
        else:
            print("Unknown command. Please try again. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()