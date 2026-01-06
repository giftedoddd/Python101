from src.modules.config import FILE_PATH

def save_to_file(username, password):
    try:
        with open(FILE_PATH, mode="a") as password_file:
            password_file.write(
                f"USERNAME,{username},PASSWORD,{password}\n"
            )
    except Exception as e:
        print(f"Failed to write passwords to file, {e}.")
        exit(100)

def read_file():
    try:
        with open(FILE_PATH, mode="r") as password_file:
            return password_file.readlines()
    except Exception as e:
        print(f"Failed to read passwords file, {e}.")
        exit(100)

def remove_from_file(lines):
    try:
        with open(FILE_PATH, mode="w") as password_file:
            password_file.writelines(lines)
    except Exception as e:
        print(f"Failed to write to passwords file, {e}.")
        exit(100)
