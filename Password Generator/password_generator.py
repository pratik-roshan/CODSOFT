import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    
    if use_lowercase:
        characters += string.ascii_lowercase
    
    if use_digits:
        characters += string.digits
    
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        print("Error: No character set selected. Please enable at least one option.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Error: Password length should be a positive integer.")
        
        else:
            use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
            use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
            
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
            if password:
                print("Generated Password: " + password)
    
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    
    except KeyboardInterrupt:
        print("\nOperation aborted by the user.")

if __name__ == "__main__":
    main()