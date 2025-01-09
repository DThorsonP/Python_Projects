alphabet = list(map(chr, range(97, 123)))

# direction = input("Type (encode) to encrpyt type (decode) to decrypt:\n")
# text = input("Type your  message:\n").lower()
# shift = int(input("Type the amount of shift:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:

        if letter not in alphabet:
            output_text += letter

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here's the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type (encode) to encrpyt type (decode) to decrypt:\n")
    text = input("Type your  message:\n").lower()
    shift = int(input("Type the amount of shift:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type yes if you want to go again. Otherwise type no\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
    