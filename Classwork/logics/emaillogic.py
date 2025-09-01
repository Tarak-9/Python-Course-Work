import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"  # fixed typo
SMTP_PORT = 587
SENDER_EMAIL = "chalapathitaraka@gmail.com"
SENDER_PASSWORD = "onab omxm pmov sxnp"  # better: os.getenv("GMAIL_APP_PASSWORD")

def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email  # fixed "TO" -> "To"
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())  # fixed
        server.quit()
        print(f" Email sent to {to_email}")

    except Exception as e:
        print(f" Error sending mail to {to_email}: {e}")

def send_bulk_emails(csv_file, subject, body):
    try:
        csv_path = os.path.abspath(csv_file)
        if not os.path.exists(csv_path):
            print(f" Error: CSV file '{csv_file}' not found.")
            return
        
        with open(csv_path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header
            for row in reader:
                if row:
                    email = row[0].strip()
                    if email:  # avoid empty rows
                        send_email(email, subject, body)

    except Exception as e:
        print(f" Error reading CSV file: {e}")
