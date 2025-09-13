# Import the random module to generate random selections
import random

# Define a string containing all possible characters for the password
# Includes lowercase, uppercase, digits, and special symbols for strength
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?/`~ "

# Print a welcome message for the user
print("Welcome to the Password Generator!")

# Get the desired password length from the user and convert it to an integer
len_of_password = int(input("Enter the length of the password: "))

# Initialize an empty string to build the password
password = ""

# Check if the requested password length meets the minimum security requirement
if len_of_password < 8:
    # Inform the user and exit if the password is too short
    print("Password length should be at least 8 characters.")
else:
    # If the length is valid, generate the password
    # Loop for the same number of times as the requested password length
    for a in range(len_of_password):
        # Randomly select one character from the 'characters' string and add it to the password
        password += random.choice(characters)
    
    # Print the final generated password
    print("Generated password is:", password)

# Print a farewell message
print("Thank you for using the password generator! Have a great day!")
