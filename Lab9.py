# Program Name: Lab9.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab9
# Due Date: 11/10/2024
# Purpose: This program verifies if a password meets the required criteria,
# including length, character type, and special character presence.
# List specific resources used to complete the assignment: None

import re

# Function to validate the password
def is_valid_password(password):
    # Check if password has at least 9 characters
    if len(password) < 9:
        return False
    # Check if password contains at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    # Check if password contains at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    # Check if password contains at least one digit
    if not re.search(r"[0-9]", password):
        return False
    # Check if password contains at least one special character (#, !, $, _)
    if not re.search(r"[#!$_]", password):
        return False
    return True

# Prompt the user to enter a password
password = input("Password: ")

# Check if the password is valid and display appropriate message
if is_valid_password(password):
    print("Valid Password")
else:
    print("Invalid Password")
