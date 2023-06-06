# Author: Ifedayo Akinsira-Olumide
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    solution = ""
    len_alphabet = len(alphabet)
    for i in range(len(text)):
        if text[i] not in alphabet:
            solution += text[i]
        else:
            new_index = alphabet.index(text[i]) + shift
            if new_index < len_alphabet:
                output_index = alphabet.index(text[i]) + shift
            else:
                output_index = len_alphabet - 2 - alphabet.index(text[i]) + shift
            #output_index = alphabet.index(text[i + shift
            solution += alphabet[output_index]
            # print(solution)
    print(f"Here is the encode result: {solution}")


def decrypt(text, shift):
    solution = ""
    for i in range(len(text)):
        if text[i] == " ":
            solution += " "
        else:
            output_index = alphabet.index(text[i]) - shift
            #output_index = alphabet.index(text[i + shift
            solution += alphabet[output_index]
    print(f"Here is the decoded result: {solution}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("You entered incorrect input")
decision = input("Type 'yes' if you want to go again otherwise type 'no' ").lower()

while decision == "yes":
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("You entered incorrect input")
    decision = input("Type 'yes' if you want to go again otherwise type 'no' ").lower()




    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
