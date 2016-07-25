
def get_cipherletter(new_key,letter):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if letter in alpha:
        letter_index = (new_key)
        return alpha[letter_index]
    else:
        return + letter
    
    

def encrypt(key, message):
    # key = 1
    # message = "IFMMP UIFSF"
    
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    for letter in message:
        new_key = (alpha.find(letter) + key) % 26
        result = result + get_cipherletter(new_key,letter)
    return result

def decrypt(key, message):
    # key = 1
    # message = "IFMMP UIFSF"
    
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    for letter in message:
        new_key = (alpha.find(letter) - key) % 26
        result = result + get_cipherletter(new_key,letter)
    return result
# do()