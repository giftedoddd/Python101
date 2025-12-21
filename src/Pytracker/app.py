from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from config import *
import hashlib
import segno
import csv

app = Flask(__name__)
app.secret_key = SECRET


def generate_qr():
    img = segno.make(TARGET_URL)
    img.save(QR_FILE, border=2, scale=10)


def get_fingerprint(req):
    ip = req.remote_addr or ""
    ua = req.headers.get("User-Agent", "")
    lang = req.headers.get("Accept-Language", "")
    raw = f"{ip}|{ua}|{lang}|{SECRET}"
    return hashlib.sha256(raw.encode()).hexdigest()


@app.route("/")
def home():
    generate_qr()
    return render_template("home.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        fingerprint = get_fingerprint(request)

        if fingerprint in submitted_fingerprints:
            session["message"] = "Attendance already submitted."
            session["status"] = "error"
            return redirect(url_for("submit"))

        name = request.form.get("name", "").strip()
        student_id = request.form.get("student_id", "").strip()

        if not name or not student_id:
            session["message"] = "Name and Student ID are required."
            session["status"] = "error"
            return redirect(url_for("submit"))

        timestamp = datetime.now().isoformat()
        csv_writer.writerow([name, student_id, fingerprint, timestamp])
        submitted_fingerprints.add(fingerprint)

        session["message"] = "Attendance recorded successfully!"
        session["status"] = "success"
        return redirect(url_for("submit"))

    message = session.pop("message", None)
    status = session.pop("status", None)
    return render_template("submit.html", message=message, status=status)


if __name__ == "__main__":
    submitted_fingerprints = set()
    records_file = open(DATA_FILE, "w", newline="", buffering=1)
    csv_writer = csv.writer(records_file)
    csv_writer.writerow(["name", "student_id", "fingerprint", "timestamp"])
    try:
        app.run(host=HOST, port=PORT, debug=DEBUG)
    finally:
        records_file.close()
