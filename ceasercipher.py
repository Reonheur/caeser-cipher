# Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to check the action encode or decode and shift the letter only in alphabet
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""  # Stores the text from user
    if encode_or_decode == "decode":  # Shift the letter backward
        shift_amount *= -1

    for letter in original_text:  # Anything that's not in alphabet will be added to the text and not be decoded
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount  #  find the Position of the alphabet plus the number to shift
            shifted_position %= len(alphabet)  #  Modulo helps keep the index within the bounds of the alphabet
            output_text += alphabet[shifted_position]  # The shifted letter is added to output_text
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True  # If the user wants to continue playing to restart
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)  # Call the function
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye Thanks for your participation")