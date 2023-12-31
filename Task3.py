import random
import string

# Function to generate a random password
def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ""
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to get user input and generate a password
def main():
    print("Password Generator")
    length = int(input("Enter the length of the password: "))
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
