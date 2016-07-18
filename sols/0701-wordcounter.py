# f = open('../drafts/_sources/resource/exclude.txt')
# x = f.read().split("\n")
# f.close()

# for i in range(len(x)):
#     x[i] = x[i].upper()

# f = open('../drafts/_sources/resource/exclude.txt','w')
# f.write('\n'.join(x))
# f.close()

LETTERS_AND_SPACE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
F_PATH = '../drafts/_sources/resource/'
READ_NAME = 'thegambler.txt'
EXCLUDE_NAME = 'exclude.txt'

def read_text():
    f = open(F_PATH + READ_NAME)
    text = f.read().replace("\n"," ").upper()
    text = remove_extra_chars(text)
    return text

#removes anything thats not a space or a letter
def remove_extra_chars(text):
    newtext = ""
    for ch in text:
        if ch in LETTERS_AND_SPACE:
            newtext = newtext + ch
            
    words = newtext.split(" ")

    while "" in words:
        words.remove("")
        
    return words

#counts the frequency of words
def count_words(text):
    wordcount = {}
    for word in text:
        if word in wordcount:
            wordcount[word]+=1
        else:
            wordcount[word]=1
    
    return wordcount

#removes stop words from dictionary wordcount
def exclude_words(wordcount):
    f = open(F_PATH + EXCLUDE_NAME)
    exclude = f.read().split("\n")
    
    for word in exclude:
        wordcount.pop(word,None)

#prints top num counted
def print_top(wordcount,num):
    for x in range(num):
        m = max(wordcount, key=wordcount.get)
        print("{}: {}".format(m,wordcount[m]))
        wordcount.pop(m)
    
    print("Total Unique Words: {}".format(len(wordcount)))

def main():
    text = read_text()
    count = count_words(text)
    exclude_words(count)
    print_top(count,20)

if __name__ == "__main__":
    main()