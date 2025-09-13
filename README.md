# 🔐 PyPassGen - Random Password Generator

A simple, yet effective, command-line password generator built in Python. This tool creates strong and random passwords to help you improve your online security.

## ✨ Features

*   **Customizable Length:** Generate passwords of any length (enforces a minimum of 8 characters for security).
*   **Strong Character Set:** Uses a comprehensive mix of:
    *   Lowercase letters (a-z)
    *   Uppercase letters (A-Z)
    *   Numbers (0-9)
    *   Special symbols (!@#$%^&*...)
*   **Simple CLI Interface:** Easy to use—just run the script and enter your desired length.
*   **No Dependencies:** Built with Python's standard library (`random` module), so no extra installations are needed.

## 🚀 How to Use

1.  **Clone the repository** or download the `password_generator.py` file.
    ```bash
    git clone https://github.com/your-username/PyPassGen.git
    ```
2.  **Navigate to the project directory.**
    ```bash
    cd PyPassGen
    ```
3.  **Run the Python script.**
    ```bash
    python password_generator.py
    ```
4.  **Follow the prompt:** Enter the desired length for your new password when asked.
5.  **Copy your password:** The generated password will be printed to the terminal. Use it to secure your accounts!

## 📝 Code Overview

The core logic is straightforward:

python
import random

# Define the character set to use for generating passwords
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?/`~ "

# Get user input for password length
len_of_password = int(input("Enter the length of the password: "))
password = ""

# Generate the password
for a in range(len_of_password):
    if len_of_password < 8:
        print("Password length should be at least 8 characters.")
        break
    else:
        password += random.choice(characters)

# Output the result
print("Generated password is:", password)
