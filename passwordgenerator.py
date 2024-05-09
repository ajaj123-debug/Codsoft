import random
import string

def generate_password(length):
    # Define character sets for different complexities
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets based on complexity
    all_chars = lower_case + upper_case + digits + special_chars

    # Generate password using random.choice() function
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for desired password length
        length = int(input("Enter the desired length of the password: "))

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
