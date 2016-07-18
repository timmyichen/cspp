from transposition import decrypt

msg = "aeeeiywvyhhil  nnoiicoevwagdtuloh reasusarllokeay y i  epn dsi uncbnaoys fwpioettwogc h nd  hsusotomgeap   hdh a   swwlk"
for x in range(1,len(msg)):
    print("Trying key #{}: {}".format(x,decrypt(x,msg)[:55]+"..."))