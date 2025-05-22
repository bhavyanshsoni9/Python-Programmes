import random
from time import sleep

# Define character sets for password generation
symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', "<", ">", ",", ".", "/", "?"]
numbers = [str(i) for i in range(100)]  # Convert numbers to strings
lowercase = [chr(i) for i in range(97, 123)]  # a-z
uppercase = [chr(i) for i in range(65, 91)]  # A-Z
password = ''.join(random.choice(numbers + uppercase))
print(password)
print("Welcome To HACKER SIMULATOR 🐱‍💻!\n")
sleep(1.5)

device = input("Enter Name Of Device to HACK: ")
sleep(1.5)

print("*** INITIATING BREACH SEQUENCE ***")
sleep(1.5)

print(f"---HACKING {device}---")
sleep(1.5)

print("Bypassing Firewall...")
sleep(1.5)

print("Bypassing Antivirus...")
sleep(1.5)

print("Bypassing Security...")
sleep(1.5)

print("Bypassing Encryption...")
sleep(1.5)

print("[✓] Accessing system logs...")
sleep(1.5)

print("[!] Firewall triggered - Solve the puzzle to bypass!")
sleep(1.5)

hint = f"Hint: The password is a combination of numbers and uppercase letters. It is {len(password)} characters long."
print(hint)
sleep(1.5)

puzzle = input("Enter the password to bypass the firewall: ")
sleep(1.5)

if puzzle == password:
    print(f"Correct You HACKED the Device {device}...")

else:
    print("You Failed! Police Caught You 🚔")