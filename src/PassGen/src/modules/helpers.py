def search(name, password_list):
    for item in password_list:
        creds = item.split(",")
        if creds[1] == name:
            return creds[3].strip()
    return None

def remove_from_list(name, password_list: list):
    list_length = len(password_list)
    index = 0
    while index < list_length:
        current_item = password_list[index]
        username = current_item.split(",")[1]
        if username == name:
            password_list.pop(index)
            return password_list

    return password_list
