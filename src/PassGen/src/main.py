def print_help():
    help_message = \
        """
    PassGen: Random Password Generator Program
    Usage:
        create [USERNAME] [PASSWORD]
        Saves a username and password provided by user to disk.
    
        create [USERNAME]
        Generates a random password and saves it to disk with username.
    
        get [USERNAME]
        Fetchs a password from disk.
    
        remove [USERNAME]
        removes a username and password from disk."""

    print(help_message)


def validate_configs():
    if not 6 <= PASSWORD_LENGTH <= 16:
        return False

    includes = UPPERCASE_LETTER or LOWERCASE_LETTER or SYMBOLS or NUMBERS
    if not includes:
        return False

    if not FILE_PATH:
        return False

    return True


def main():
    print("Welcome to PassGen program.")

    if not validate_configs():
        print("Failed to validate configuration file.")
        exit(100)

    print("Enter the operation.")
    while True:
        op = input(">> ")

        if op == "help":
            print_help()
            continue

        elif op == "exit":
            print("Goodbye!")
            exit(0)

        elif op.startswith("create"):
            input_list = op.split(" ")
            if not 2 <= len(input_list) <= 3:
                print("Wrong number of argument.")
                print_help()
                continue

            username = input_list[1]
            if len(input_list) == 3:
                password = input_list[2]
            else:
                password = generate()

            creds = read_file()
            if search(username, creds):
                print("This username already saved.")
                continue

            save_to_file(username, password)

        elif op.startswith("get"):
            input_list = op.split(" ")
            if not len(input_list) == 2:
                print("Wrong number of argument.")
                print_help()
                continue

            password_list = read_file()
            if not password_list:
                print("Password file is empty, Create a password first.")
                continue

            username = input_list[1]
            result = search(username, password_list)
            if result is None:
                print("No password found.")
                continue

            print(result)

        elif op.startswith("remove"):
            input_list = op.split(" ")
            if not len(input_list) == 2:
                print("Wrong number of argument.")
                print_help()
                continue

            password_list = read_file()
            if not password_list:
                print("Password file is empty, Create a password first.")
                continue

            username = input_list[1]
            result = search(username, password_list)
            if result is None:
                print("No password found.")

            new_list = remove_from_list(username, password_list)
            remove_from_file(new_list)
        else:
            print("Invalid input try again, Enter help to see help menu.")


if __name__ == '__main__':
    main()
