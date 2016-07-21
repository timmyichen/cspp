from transposition import decrypt
from detectEnglish import is_english

msg = "aeeeiywvyhhil  nnoiicoevwagdtuloh reasusarllokeay y i  epn dsi uncbnaoys fwpioettwogc h nd  hsusotomgeap   hdh a   swwlk"
for key in range(1,len(msg)):
    decryption = decrypt(key,msg)
    print("Trying key #{}: {}".format(key,decryption[:55]+"..."))
    if is_english(decryption):
        choice = input("Found potential solution with key {}, enter 'X' to exit or just press Enter to continue: ".format(key))
        if choice.upper() == 'X':
            print("Ending.  The selected key is {}".format(key))
            print("The selected solution is: \n{}".format(decryption))
            break