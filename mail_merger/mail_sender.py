# NOTE: Used to send the mail to the recipient email id

# importing all necessary files
import excel_sheet_reader
import gen_ai_mail
# importing all necessary modules
import smtplib
from email.message import EmailMessage
import os
import sys  # Import sys to exit the program if needed


def send_email(sender_email, receiver_email, subject, body):
    app_password = os.getenv('mail_merge_smtp_password')

    # Check if app_password is None
    if app_password is None:
        print("Error: The environment variable 'mail_merge_smtp_password' is not set.")
        sys.exit(1)  # Exit the program with an error code

    # SMTP setup
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Start SMTP connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, app_password)

    # Send the email
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        server.send_message(msg)
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {e}")
    finally:
        # Close server
        server.quit()

if __name__ == "__main__":
    pass