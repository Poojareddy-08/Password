import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    # Prompt the user for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Generate and display the password
    password = generate_password(length)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
