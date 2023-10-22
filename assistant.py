def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def hello():
    return 'How can I help you?'

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact updated.'

def show_phone(args, contacts):
    name = args[0].lower()
    try:
        return contacts[name]
    except:
        return 'Not found'

def show_all(contacts):
    result = ''
    for name, phone in contacts.items():
        result += f"{name.title()} {phone}\n"
    return result


def main():
    contacts = {}

    methods = {
        'hello': hello,
        'add': add_contact,
        'change': change_contact,
        'phone': show_phone,
        'all': show_all,
    }

    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command:').strip().lower()
        command, *args = parse_input(user_input)

        if command in methods.keys():
            if (len(args) > 0):
                print(methods[command](args, contacts))
            else:
                print(methods[command](contacts))
            continue

        if command in ['close', 'exit']:
            print("Good bye!")
            break

        print('Invalid command.')

if __name__ == "__main__":
    main()

            