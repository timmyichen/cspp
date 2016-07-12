"""
set 3 main variables - key, message, action


"""
def do(key, message, action):
    # key = 1
    # message = "IFMMP UIFSF"
    # action = "decrypt" #encrypt or decrypt
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = ""
    
    for letter in message:
        if letter in alpha:
            letter_index = alpha.find(letter)
            if action == "encrypt":
                letter_index = letter_index + key
                if letter_index > len(alpha)-1:
                    letter_index = letter_index - len(alpha)
            else:
                letter_index = letter_index - key
                if letter_index < 0:
                    letter_index = letter_index + len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    print(result)

do()