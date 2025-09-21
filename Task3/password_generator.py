# Password Generator Application

import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generates a password based on user-defined criteria."""
    
    # Define character sets based on user choices
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # includes both lower and upper case
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: You must select at least one character type.")
        return None

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("--- PASSWORD GENERATOR ---")
    
    try:
        # Get password length from user
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return

        # Get complexity choices from user
        use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        # Generate and display the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        if password:
            print(f"\nYour Generated Password is: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")

if __name__ == "__main__":
    main()