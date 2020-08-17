# Import Libraries and Functions
from sys import argv, exit
from alpha import test_alpha

# If command-line argument is not correct!
if len(argv) != 2:

    # Print Error, Exit the program
    print("\nEnter Key from (1 - 25) with run command!\n")
    exit(1)

# Convert key to int
key = int(argv[1])

# If range of key is not correct
if key < 1 or key > 25:

    # Print Error, Exit the program
    print("\nEnter Correct Key in range (1 - 26)\n")
    exit(2)

# Keep prompting till valid input
while (True):

    # Ask for user input
    plaintext = input("\nPlaintext: ")

    # Pass input string to function
    check = test_alpha(plaintext)

    # If function returns True, Exit the loop
    if check == True:
        break
    
    # If not correct input is supplied
    print("\nEnter Correct Text!\n")

# List to store ciphered chars
ciphertext = []

# Iterate character by character
for i in range(len(plaintext)):

    # Get ASCII value of char
    ascii_val = ord(plaintext[i])

    # If Uppercase
    if ascii_val >= 65 and ascii_val <= 90:

        # Encrypt the char with user key, Store in the list
        char_cipher = ((((ascii_val + key) - 65) % 26) + 65)
        ciphertext.append(chr(char_cipher))

    # If Lowercase
    if ascii_val >= 97 and ascii_val <= 122:

        # Encrypt the char with user key, Store in the list
        char_cipher = ((((ascii_val + key) - 97) % 26) + 97)
        ciphertext.append(chr(char_cipher))

    # If ith char is space
    if plaintext[i] == " ":

        ciphertext.append(" ")

# String to store ciphered chars
text = ""

# Iterate through each char in the list
for i in range(len(ciphertext)):

    # Store char in string
    text += ciphertext[i]

# Print Ciphertext, Exit Successfully
print("Ciphertext: ", text, "\n")
print("Developed By Syed Shehroz Ali")
exit(0)
    




