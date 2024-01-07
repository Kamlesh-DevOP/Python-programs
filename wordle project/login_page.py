from tkinter import *
import re

root1 = Tk()
root1.title("Login Page")

def login():
    username = username_entry.get()
    password = password_entry.get()

def validate_credentials(username, password):
    # Replace with your actual authentication logic
    if username == "user" and password == "password" and is_strong_password(password):
        return True
    return False

strength_colors = {
    "Weak": "red",
    "Medium": "orange",
    "Strong": "green"}  # Define the strength colors

def check_password_strength(password):
    # Example password strength check logic
    strength_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if len(password) < 8 and not re.match(strength_regex, password):
        return 'Weak'
    else: return "Strong"
    
def is_strong_password(password):
    # Example password strength check
    strength_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return re.match(strength_regex, password)

    # Validate credentials (replace with your authentication logic)
    if validate_credentials(username, password):
        success_label.config(text="Login successful!")
        password_entry.delete(0,  END)  # Clear password field
        root1.destroy()
    else:
        error_label.config(text="Invalid username or password")


# Username label and entry
username_label =  Label(root1, text="Username:")
username_label.pack()
username_entry =  Entry(root1)
username_entry.pack()

# Password label and entry
password_label =  Label(root1, text="Password:")
password_label.pack()
password_entry =  Entry(root1, show="*")  # Hide password characters
password_entry.pack()

# Login button
login_button =  Button(root1, text="Login", command=login)
login_button.pack()

# Labels for feedback
success_label =  Label(root1, text="")
success_label.pack()
error_label =  Label(root1, text="", fg="red")  # Display errors in red
error_label.pack()

# Enhanced UI elements
password_strength_label =  Label(root1, text="Password Strength:")
password_strength_label.pack()
password_strength_indicator =  Label(root1, text="", fg="gray")  # Initially gray
password_strength_indicator.pack()

# Update password strength indicator as the user types
def update_password_strength(event):
    strength = check_password_strength(password_entry.get())
    password_strength_indicator.config(text=strength, fg=strength_colors[strength])

password_entry.bind("<Key>", update_password_strength)