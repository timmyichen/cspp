import math
import random

def encrypt(key,message):
    # figure out # of rows
    rows = math.ceil(len(message) / key)
    cols = key
    
    table = [[''] * cols for i in range(rows)]
    
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    pointer = 0
    
    encrypted = ''
    
    for r in range(rows):
        for c in range(cols): #rows[r] is column
            if pointer < len(message):
                #print("assigning {} into r{}c{}".format(message[pointer],r,c))
                table[r][c] = message[pointer]
            else:
                rand_letter = random.choice(letters)
                #print("assigning random {} into r{}c{}".format(rand_letter,r,c))
                table[r][c] = rand_letter
                
            pointer = pointer + 1
    
    for c in range(cols):
        for r in range(rows):
            encrypted = encrypted + table[r][c]
        
    return encrypted

def decrypt(key,message):
    
    rows = math.ceil(len(message)/key)
    cols = key
    
    table = [[''] * cols for i in range(rows)]
    
    pointer = 0
    
    decrypted = ''
    
    for c in range(cols):
        for r in range(rows):
            if pointer < len(message):
                table[r][c] = message[pointer]
            else:
                break
            pointer = pointer + 1
    
    for r in range(rows):
        for c in range(cols):
            decrypted = decrypted + table[r][c]
            
    return decrypted
    
    # return table

def main():
    #message = "always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"
    message = "aeeeiywvyhhil  nnoiicoevwagdtuloh reasusarllokeTy y i  epn msi uncbnaoyZ fwpioettwodc h nd  hsuOotomgeap   Pdh a   swwlw"
    key = 10
    #print(encrypt(key,message))
    
    # table =  decrypt(key,message)
    print(decrypt(key,message))
    
    # for row in table:
    #     print(row)

if __name__ == "__main__":
    main()