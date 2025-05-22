import random

# Define character sets for password generation
symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', "<", ">", ",", ".", "/", "?"]
numbers = [str(i) for i in range(100)]  # Convert numbers to strings
lowercase = [chr(i) for i in range(97, 123)]  # a-z
uppercase = [chr(i) for i in range(65, 91)]  # A-Z

def generate_or_store():
    # Prompt user for action
    g_o_s = input("Do you want to generate a password or store a password? (g/s): ").strip().lower()
    
    if g_o_s == "g":
        try:
            # Get password length from user
            password_length = int(input("Enter the length of the password: "))
            if password_length <= 0:
                print("Password length must be greater than 0.")
                return
            
            # Generate password
            password = ''.join(random.choice(symbols + numbers + lowercase + uppercase) for _ in range(password_length))
            print(f"Password generated: {password}")
        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.")
    
    elif g_o_s == "s":
        # Get site, username, and password from user
        name = input("Enter the name of the site: ").strip()
        user_name = input("Enter the username: ").strip()
        password = input("Enter the password: ").strip()
        
        # Store the credentials in a file
        with open("passwords.txt", "a") as f:
            f.write(f"Site: {name}, Username: {user_name}, Password: {password}\n")
        print("Password stored successfully.")
    
    else:
        # Handle invalid input
        print("Invalid input. Please enter 'g' to generate or 's' to store a password.")

# Run the function
generate_or_store()