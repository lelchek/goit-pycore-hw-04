def parse_input(user_input: str):
    parts = user_input.split()

    if not parts:
        return "", []

    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    args = [arg.lower().strip() for arg in args]

    return cmd, args


def greeting():
    return "How can I help you?"


def add_contact(name, phone, contacts):
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Error: Contact already exists"


def change_contact(name, phone, contacts):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: Contact does not exist"


def show_phone(name, contacts):
    if name in contacts:
        return f"Phone number for {name} is {contacts[name]}."
    else:
        return "Error: Contact does not exist"


def show_all(contacts):
    if not contacts:
        return "No contacts found."

    contact_list = ""

    for name, phone in contacts.items():
        contact_list += f"{name}: {phone}\n"

    return contact_list


def validate(command: str, args):
    match command:
        case "add" | "change":
            return len(args) == 2

        case "phone":
            return len(args) == 1

        case _:
            return True


def bye():
    return "Good bye!"


def main():
    contacts = {}
    error_text = "Error: Not enough arguments"

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        match command:
            case "hello":
                print(greeting())

            case "add":
                if validate("add", args):
                    name, phone = args
                    print(add_contact(name, phone, contacts))

                else:
                    print(error_text)

            case "change":
                if validate("change", args):
                    name, phone = args
                    print(change_contact(name, phone, contacts))

                else:
                    print(error_text)

            case "phone":
                if validate("phone", args):
                    name = args[0]
                    print(show_phone(name, contacts))

                else:
                    print(error_text)

            case "all":
                print(show_all(contacts))

            case "close" | "exit":
                print(bye())
                break

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
