# Rot cipher decoder

# All based on the alphabet
alpha = 'abcdefghijklmnopqrstuvwxyz'

# Ask for encoded message
encoded = input('Enter the encoded string: ')
# Change input to lowercase
enc_var = encoded.lower()

# Key Variable (rot1 - 25)
key = range(1,26)

# Printout description header
print('ROT', '-','Decoded String')

# For loop (for each key value)
for num in list(key):
    # Clear variable for each run
    decoded_msg = None
    # Variable to store new decoded message
    decoded_msg = ''

    # For loop (for each encoded letter)
    for char in enc_var:
        # Ignore spaces and non-alpha chars
        if char in alpha:
            # Get the position of the letter
            pos = alpha.find(char)
            # Change to new position based on key ("% 26" rolls over to zero after 26)
            new_pos = (pos + num) % 26
            # Get the letter associated with the new position
            decoded = alpha[new_pos]
            # add the letters together
            decoded_msg += decoded
        else:
            # Otherwise, insert original char
            decoded_msg += char

        # What rot var was used
        encodedkey = 26 - num
    print(encodedkey,'-', decoded_msg)