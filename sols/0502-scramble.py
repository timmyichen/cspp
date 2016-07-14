import random

def scramble(word):
    if len(word) < 4:
        return word
    else:
        possible_letters = list(word[1:-1])
        
        result = ""
        
        for i in range(len(word)-2):
            rand_index = random.randint(0,len(possible_letters)-1)
            result = result + possible_letters[rand_index]
            possible_letters.remove(possible_letters[rand_index])
        
        result = word[0] + result + word[-1]
        
        if result == word:
            result = scramble(word)
        return result

def scramble_phrase(phrase):
    words = phrase.split(" ")
    result = ""
    for word in words:
        result = result + scramble(word) + " "
    return result

def main():
    print(scramble_phrase("I love learning computer science"))
    print(scramble_phrase("I love learning computer science"))
    print(scramble_phrase("I love learning computer science"))
    print(scramble_phrase("I love learning computer science"))
    print(scramble_phrase("I love learning computer science"))

if __name__ == "__main__":
    main()