def search(name, password_list):
    for item in password_list:
        creds = item.split(",")
        if creds[1] == name:
            return creds[3].strip()
    return None

