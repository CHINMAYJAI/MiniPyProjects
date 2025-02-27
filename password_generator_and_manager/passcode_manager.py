# importing necessary modules

# tkinter for GUI
import tkinter as tk

# messagebox for showing message box
from tkinter import messagebox
from tkinter import PhotoImage

# passcode_generator for generating strong passcode
import passcode_generator
import re  # regular expression
# datetime for getting current date and time and setting at which time the passcode is created and password is updated
import datetime
# use to generate random string in salt which is use to set if the passcode is identical then in that case to enhance security we use salt to make it hashes different
import random
import string  # to generate random string
# setting up the connection with mongoDB
import pymongo
from pymongo import MongoClient
# for security we use hash function to convert the password into hashes
import hashlib
import base64
import os
# for sending email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class PasscodeManager:
    def __init__(self):
        """Use to make the connection with the mongoDB and tkinter window is created here."""
        self.client = MongoClient(
            "connectivity link"
        )  # Fixed MongoDB connection string
        self.db = self.client["passcode_manager"]
        self.collection = self.db["passcode"]
        self.email = "your_email_address"
        self.password = "your_email_password"
        self.root = tk.Tk()
        self.root.title("Passcode Manager")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")  # Set background color
        self.app_name = tk.StringVar()
        self.passcode = tk.StringVar()
        self.email_address = tk.StringVar()
        self.app_name.set("")
        self.passcode.set("")
        self.email_address.set("")
        self.create_main_menu()

    def create_main_menu(self):
        """Use to create the main menu for the tkinter window."""
        # NOTE: Styling options
        label_font = ("Helvetica", 12, "bold")
        button_font = ("Helvetica", 12, "bold")
        button_bg = "#4CAF50"
        button_fg = "#FFFFFF"

        tk.Label(
            self.root,
            text="What would you like to do?",
            font=label_font,
            bg="#2C3E50",
            fg="#ECF0F1",
        ).pack(pady=20)
        tk.Button(
            self.root,
            text="Add Passcode",
            command=self.add_passcode_menu,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
        ).pack(pady=10)
        tk.Button(
            self.root,
            text="Update Passcode",
            command=self.update_passcode_menu,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
        ).pack(pady=10)
        tk.Button(
            self.root,
            text="Check Passcode",
            command=self.check_passcode_menu,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
        ).pack(pady=10)

        # Add "logoCJ.png" logo
        logo = PhotoImage(file="assets/logoCJ.png").subsample(
            4, 4
        )  # Further decrease the size of the logo
        self.logo_label = tk.Label(self.root, image=logo, bg="#2C3E50")
        self.logo_label.image = logo  # Keep a reference to avoid garbage collection
        self.logo_label.pack(side="bottom", pady=10)

        # Add information label
        tk.Label(
            self.root,
            text="Note: Passwords cannot be retrieved. You can only change them by providing the application name and email address.",
            font=("Helvetica", 10),
            bg="#2C3E50",
            fg="#ECF0F1",
            wraplength=350,
        ).pack(pady=10)

    def add_passcode_menu(self):
        """Use to create the add passcode menu."""
        self.clear_window()
        self.create_widgets("Add Passcode", self.enter)

    def update_passcode_menu(self):
        """Use to create the update passcode menu."""
        self.clear_window()
        self.create_widgets("Update Passcode", self.update_passcode)

    def check_passcode_menu(self):
        """Use to create the check passcode menu."""
        self.clear_window()
        self.create_widgets("Check Passcode", self.check_passcode)

    def create_widgets(self, action, command, show_passcode=True):
        """Use to create the widgets for the tkinter window."""
        # NOTE: Styling options
        label_font = ("Helvetica", 12, "bold")
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12, "bold")
        button_bg = "#4CAF50"
        button_fg = "#FFFFFF"

        tk.Label(
            self.root,
            text="Application Name:",
            font=label_font,
            bg="#2C3E50",
            fg="#ECF0F1",
        ).pack(pady=5)
        tk.Entry(self.root, textvariable=self.app_name, font=entry_font).pack(pady=5)
        tk.Label(
            self.root, text="Passcode:", font=label_font, bg="#2C3E50", fg="#ECF0F1"
        ).pack(pady=5)
        tk.Entry(
            self.root, textvariable=self.passcode, show="*", font=entry_font
        ).pack(pady=5)
        if show_passcode and action != "Check Passcode":
            tk.Button(
                self.root,
                text="Generate Strong Passcode",
                command=self.suggest_passcode,
                font=button_font,
                bg=button_bg,
                fg=button_fg,
            ).pack(pady=5)
        tk.Label(
            self.root,
            text="Email Address:",
            font=label_font,
            bg="#2C3E50",
            fg="#ECF0F1",
        ).pack(pady=5)
        tk.Entry(self.root, textvariable=self.email_address, font=entry_font).pack(
            pady=5
        )
        tk.Button(
            self.root,
            text=action,
            command=command,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
        ).pack(pady=10)
        tk.Button(
            self.root,
            text="Back",
            command=self.back_to_main_menu,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
        ).pack(pady=10)

    def clear_window(self):
        """Use to clear the tkinter window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def back_to_main_menu(self):
        """Use to go back to the main menu."""
        self.clear_window()
        self.create_main_menu()

    def suggest_passcode(self):
        """Use to suggest a strong passcode."""
        # Use to suggest the passcode by using the passcode_generator module
        strong_passcode = passcode_generator.generate_strong_passcode()
        if messagebox.askyesno(
            "Suggested Passcode",
            f"Suggested Passcode: {strong_passcode}\nDo you want to use this passcode?",
        ):
            self.passcode.set(strong_passcode)

    def enter(self):
        """Use to store the passcode in the mongoDB."""
        if (
            self.app_name.get() == ""
            or self.passcode.get() == ""
            or self.email_address.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required!")
        else:
            if self.validate_email(self.email_address.get()):
                self.store_passcode()
            else:
                messagebox.showerror("Error", "Invalid email address!")

    def validate_email(self, email):
        """Use to validate the email address."""
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    def store_passcode(self):
        """Use to store the passcode in the mongoDB."""
        passcode = self.passcode.get()
        # sometimes it might be possible that the passcode is same so to make hashes unique we use salt
        salt = self.generate_salt()
        passcode = passcode + salt
        # converting the passcode into hash
        passcode = self.hash_passcode(passcode)
        # storing the data in the mongoDB
        data = {
            "app_name": self.app_name.get(),
            "passcode": passcode,
            "email_address": self.email_address.get(),
            "salt": salt,
            "created_at": datetime.datetime.now(),
        }
        self.collection.insert_one(data)
        self.send_email()
        self.app_name.set("")
        self.passcode.set("")
        self.email_address.set("")
        messagebox.showinfo("Success", "Passcode stored successfully!")

    def generate_salt(self):
        """Use to generate the salt."""
        return "".join(random.choices(string.ascii_letters + string.digits, k=8))

    def hash_passcode(self, passcode):
        """Use to convert the passcode into hash."""
        return hashlib.sha256(passcode.encode()).hexdigest()

    def send_email(self):
        """Use to send the email."""
        # sending the email to the user that the passcode is stored successfully
        try:
            msg = MIMEMultipart()
            msg["From"] = self.email
            msg["To"] = self.email_address.get()
            msg["Subject"] = "Passcode Manager"
            body = "Your passcode has been stored successfully!"
            msg.attach(MIMEText(body, "plain"))
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, self.email_address.get(), text)
            server.quit()
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", "Failed to send email: Incorrect username or password.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")

    def update_passcode(self):
        """Use to update the passcode in the mongoDB."""
        # it will just take the entries from the user
        if (
            self.app_name.get() == ""
            or self.passcode.get() == ""
            or self.email_address.get() == ""
        ):
        # if any of the field is empty then show the error message
            messagebox.showerror("Error", "All fields are required!")
        else:
            # if the email address is valid then update the passcode
            if self.validate_email(self.email_address.get()):
                self.modify_passcode()
            else:
                messagebox.showerror("Error", "Invalid email address!")

    def modify_passcode(self):
        """Use to modify the passcode in the mongoDB."""
        # it will update the passcode on the basis of the entries enter by the user
        passcode = self.passcode.get()
        salt = self.generate_salt()
        passcode = passcode + salt
        passcode = self.hash_passcode(passcode)
        query = {
            "email_address": self.email_address.get(),
            "app_name": self.app_name.get(),
        }
        new_values = {
            "$set": {
                "passcode": passcode,
                "salt": salt,
                "updated_at": datetime.datetime.now(),
            }
        }
        # use to fetch the record from the database
        result = self.collection.update_one(query, new_values)
        # if the record is fetched then update the passcode
        if result.matched_count > 0:
            self.send_email()
            self.app_name.set("")
            self.passcode.set("")
            self.email_address.set("")
            messagebox.showinfo("Success", "Passcode updated successfully!")
        else:
            # if the record is not fetched then show the error message
            messagebox.showerror("Error", "No matching record found!")

    def check_passcode(self):
        """Use to check if the entered passcode is correct."""
        # if any of the field is empty then show the error message
        if (
            self.app_name.get() == ""
            or self.passcode.get() == ""
            or self.email_address.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required!")
        else:
            if self.validate_email(self.email_address.get()):
                self.verify_passcode()
            else:
                messagebox.showerror("Error", "Invalid email address!")

    def verify_passcode(self):
        """Use to verify the passcode in the mongoDB."""
        # Get the record from the database
        query = {
            "email_address": self.email_address.get(),
            "app_name": self.app_name.get(),
        }
        result = self.collection.find_one(query)
        if result:
            entered_passcode = self.passcode.get() + result["salt"]
            entered_hashed_passcode = self.hash_passcode(entered_passcode)
            if entered_hashed_passcode == result["passcode"]:
                messagebox.showinfo("Success", "Passcode is correct!")
            else:
                messagebox.showerror("Error", "Incorrect passcode!")
        else:
            messagebox.showerror("Error", "No matching record found!")

    def main(self):
        """Use to run the application."""
        self.root.mainloop()


# Run the application
if __name__ == "__main__":
    PasscodeManager().main()
