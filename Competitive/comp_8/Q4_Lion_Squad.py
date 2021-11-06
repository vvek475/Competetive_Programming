# def input_validation(message):
#    while True:
#        user_input = input(message)
#        if user_input.isalpha or user_input[0]==' '():
#            return user_input 
#            break
#        else:   
#             print("Not an string! Try again.")
#             continue

def encode(string):
    vowel_to_number = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    return ''.join(vowel_to_number.get(char, char) for char in string)

def decode(string):
    number_to_vowel = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    return ''.join(number_to_vowel.get(char, char) for char in string)

if __name__=="__main__":
    string = input("Enter string:")
    encoded_string = encode(string)
    print("Encoded string: ", encoded_string)
    decoded_string = decode(encoded_string)
    print("Decoded string: ", decoded_string)