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

