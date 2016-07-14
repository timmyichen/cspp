def pluralize(num,word):
    if num == 1:
        print("1 {}".format(word))
    else:
        plural = ""
        if word[-2:] == "fe":
            plural = word[:-2] + "ves"
        elif word[-2:] == "ey" or word[-2:] == "ay" or word[-2:] == "uy" or word[-2:] == "oy":
            plural = word + "s"
        elif word[-1:] == "y":
            plural = word[:-1] + "ies"
        elif word[-2:] == "ch" or word[-2:] == "sh":
            plural = word + "es"
        elif word[-2:] == "us":
            plural = word[:-2] + "i"
        else:
            plural = word + "s"
        print("{} {}".format(num, plural))
    
def main():
    num = int(input("Enter a number: "))
    word = input("Enter a word in singular form: ")
    pluralize(num, word)
    
if __name__ == "__main__":
    main()