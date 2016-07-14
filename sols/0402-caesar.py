
def encrypt(key, message):
    # key = 1
    # message = "IFMMP UIFSF"
    
    message = message.upper()
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = ""
    
    for letter in message:
        if letter in alpha:
            letter_index = alpha.find(letter) + key
            
            if letter_index > len(alpha)-1:
                letter_index = letter_index - len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result

def decrypt(key, message):
    # key = 1
    # message = "IFMMP UIFSF"
    
    message = message.upper()
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = ""
    
    for letter in message:
        if letter in alpha:
            letter_index = alpha.find(letter) - key
            
            if letter_index < 0:
                letter_index = letter_index + len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result
