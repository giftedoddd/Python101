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


