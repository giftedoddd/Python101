import secrets

HOST = "192.168.1.110"
PORT = 8000
DEBUG = False
QR_FILE = "./static/qr.png"
TARGET_URL = f"http://{HOST}:{PORT}/submit"
DATA_FILE = "data/record.csv"
SECRET = secrets.token_hex(32)
