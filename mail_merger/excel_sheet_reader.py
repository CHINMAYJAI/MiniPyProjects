# NOTE: this file simply just reads the data from the excel sheet and passes the data to the gen_ai_mail.py file and note that it will update the mail status in the excel sheet that whether the mail is sent or not

# importing necessary module
import pandas as pd
import gen_ai_mail
import mail_sender 
import coloring_excel_cell_mailNotSent
# importing necessary modules
import datetime
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# fetching current date and time

# Read by default 1st sheet of an excel file
df = pd.read_excel("MailRecipients.xlsx")

# Access specific columns
receiver_names = df["ReceiverName"]
receiver_emails = df["ReceiverEmail"]
sender_names = df["SenderName"]
sender_emails = df["SenderEmail"]
posts = df["Post"]
subjects = df["CustomMessage"]

# Example: Loop through each row
for index, row in df.iterrows():
    mail_status = False
    # Extract data from the row
    receiver_name = row["ReceiverName"]
    sender_name = row["SenderName"]
    receiver_email = row["ReceiverEmail"]
    sender_email = row["SenderEmail"]
    subject = row["CustomMessage"]
    sender_post = row["Post"]

    try:
        # Call the automated mail generator and store the result
        print("Generating Mail....")
        generated_mail = gen_ai_mail.automated_mail_generator(
            receiver_name, sender_name, sender_post, subject
        )
        print("Mail Generated")
        if receiver_email == "nan" or sender_email == "nan":
            print("Cannot send the mail as mail section is empty")
        print("Sending....")
        # Send the email immediately after generating it
        mail_sender.send_email(sender_email, receiver_email, subject, generated_mail)

        print("Mail Sent!")
        print("-" * 50)
        mail_status = True
    except Exception as e:
        print(f"Error {e} occured")
    finally:
        if mail_status:
            current_date = datetime.date.today()
            current_time = datetime.datetime.now().time()
            df.at[index,'MailStatus'] = f"Sent::Date: {current_date}, Time: {current_time}"
            # Save it back to Excel
            df.to_excel('MailRecipients.xlsx', index=False)
        else:
            df.at[index,'MailStatus'] = f"Not Sent"
            df.to_excel('MailRecipients.xlsx')
            # calling the function that colors the cells on the basis of the mail status if not sent then it will color it else no color is there
            coloring_excel_cell_mailNotSent.coloringCells()