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


