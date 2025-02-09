import customtkinter as ctk
import re

def validate_email(event):
    email = emadd.get()
    # Regular expression to check the validity of the email including domain
    email_regex = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    valid_length = 5 <= len(email) <= 254
    
    if re.match(email_regex, email) and valid_length:
        feedback_label.config(image=valid_image, text="Valid Email", compound='left', fg_color="green")
    else:
        feedback_label.config(image=invalid_image, text="Invalid Email", compound='left', fg_color="red")

# Set up the main window
root = ctk.CTk()
root.title("Instant Email Validator")

# Load images using CTkImage
valid_image = ctk.CTkImage(file="path/to/valid_image.png")
invalid_image = ctk.CTkImage(file="path/to/invalid_image.png")

# Create the entry widget for email input
emadd= ctk.CTkEntry(root, font=("Helvetica", 16))
emadd.pack(padx=20, pady=20)

# Create a label for feedback
feedback_label = ctk.CTkLabel(window, text="", font=("Helvetica", 16))
feedback_label.pack(pady=10)

# Bind the validate_email function to the KeyRelease event
emadd.bind("<KeyRelease>", validate_email)

# Start the main event loop
root.mainloop()