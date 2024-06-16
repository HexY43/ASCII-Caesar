import argparse
import sys

# GLOBAL VARIABLES
MY_KEY = 23
LEAST_VALUE = 32 # SPACE
HIGHEST_VALUE = 122 # Z

def main():
    args = parse_arguments()
    if (args.b) is not None:
        bruteforce(args.b)
        sys.exit("Finished")
    else:
        if (args.e) is not None:
            if (args.k not in range(LEAST_VALUE, HIGHEST_VALUE+1)):
                sys.exit("Invalid key")
            else:
                encrypt(args.e, args.k)
        else:
            if (args.d) is not None:
                if (args.k not in range(LEAST_VALUE, HIGHEST_VALUE+1)):
                    sys.exit("Invalid key")
                else:
                    decrypt_specific_key(args.d, args.k)
    


def parse_arguments():

    parser = argparse.ArgumentParser(
        prog = "ASCII Caesar Encryption",
        description="Encrypts a message using the ASCII Caesar cipher, please visit github.com/HexY43/ASCII-Caesar for use caeses.",
        epilog="github.com/HexY43/ASCII-Caesar"
    )
    parser.add_argument("-e", help="Encrypt a message", type=str, metavar="MESSAGE")
    parser.add_argument("-d", help="Decrypt a message", type=str, metavar="MESSAGE")
    parser.add_argument("-k", help="Encryption/Decryption key", type=int, metavar="KEY")
    parser.add_argument("-b", help="Bruteforce decryption", metavar="MESSAGE")
    args = parser.parse_args()
    return args 

def encrypt(message, key):

    # Transforming each letter to its corresponding ASCII numeric value and adding it to a list
    corresponding_ascii = []
    for letter in message:
        letter = ord(letter) - 32
        corresponding_ascii.append(letter)

    # Applying CT = (E(PT), K)
    enciphered_text = []
    for ascii in corresponding_ascii:
        val = (ascii + key)
        enciphered_text.append(val%91 + 32)

    # Converting ASCII numeric value to its corresponding character
    enciphered_str = []
    for ascii in enciphered_text:
        enciphered_str.append(chr(ascii))

    ct_str = ""
    for ct in enciphered_str:
        ct_str += ct
    print(f"\n Encrypted message: {ct_str}")
    return ct_str

def decrypt_specific_key(message, key):

    # Transforming each letter to its corresponding ASCII numeric value and adding it to a list
    corresponding_ascii = []
    for letter in message:
        letter = ord(letter) - 32
        corresponding_ascii.append(letter)

    
    # Applying PT = (D(CT), K)
    deciphered_text = []
    for ascii in corresponding_ascii:
        val = (ascii - key)
        deciphered_text.append(val%91 + 32)
        
    
    # Converting ASCII numeric value to its corresponding character
    plaintext = []
    for ascii in deciphered_text:
        plaintext.append(chr(ascii))

    pt_str = ""
    for pt in plaintext:
        pt_str += pt
    print(pt_str)
    return pt_str


def bruteforce(message):

   # Try every possible key in the range of [32,122]
   for key in range(LEAST_VALUE, HIGHEST_VALUE+1):
        # Transforming each letter to its corresponding ASCII numeric value and adding it to a list
        corresponding_ascii = []
        for letter in message:
            letter = ord(letter) - 32
            corresponding_ascii.append(letter)

    
    # Applying PT = (D(CT), K)
        deciphered_text = []
        for ascii in corresponding_ascii:
            val = (ascii - key)
            deciphered_text.append(val%91 + 32)
        
    
    # Converting ASCII numeric value to its corresponding character
        plaintext = []
        for ascii in deciphered_text:
            plaintext.append(chr(ascii))

        pt_str = ""
        for pt in plaintext:
            pt_str += pt
        print(f"Key: {key} - Message: {pt_str}\n")

if __name__ == "__main__":
    main()
    # You can test with your code here.
    # cipher_text = "`7$!x. 7X((x$>/7d!//!*#!.7?g!xz!7x* 7Y(!//%*#/7Y!7l,+*7_%)@7/x5%*#7.!#x. %*#7ix)x x*Q7n$+!2!.7,.x5! 7x07*%#$07%*7%07?0$!7)+*0$7+\"7ix)x x*@7+107+\"7/%*z!.!7]x%0$7x* 7$+,%*#7\"+.7x7.!3x. 7\".+)7X((x$C70$!*7x((7$%/7,.!2%+1/7/%*/73%((7y!7\"+.#%2!*E"
    # plain_text = "I heard Allah's Messenger (Peace and Blessings Be Upon Him) saying regarding Ramadan: Whoever prayed at night in it (the month of Ramadan) out of sincere Faith and hoping for a reward from Allah, then all his previous sins will be forgiven."
    # output = encrypt(plain_text, MY_KEY)
    # print(output == cipher_text)

  
    