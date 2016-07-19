txtfiles = ['one.txt','two.txt','three.txt']
stopwords = open('../drafts/_sources/resource/exclude.txt').read().split("\n")

index = {}

INCLUDE_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789 '"

import json

def create_index(files=txtfiles):
    for file in files:
        words = open("search/"+file).read().split(" ")
        
        for i in range(len(words)):
            new_word = ""
            
            for letter in words[i]:
                if letter in INCLUDE_CHARACTERS:
                    new_word += letter
            
            new_word = new_word.lower()
            
            if new_word in index:
                if file not in index[new_word]:
                    index[new_word].append(file)
            elif new_word.upper() not in stopwords:
                index[new_word] = [file]
    try:
        savefile = open('search/search_index.json','w')
        json.dump(index,savefile)
        return "success creating index"
    except:
        return "failed creating index"

def load_index(name='search_index.json'):
    openfile = open('search/'+name, 'r')
    global index
    try:
        index = json.load(openfile)
        return "success loading index"
    except ValueError:
        return "failed loading index"
        index = {}

def search_index(search_term):
    if search_term.lower() in index:
        return index[search_term.lower()]
    else:
        return []

def print_index():
    print(index)

def main():
    print(create_index())
    print(load_index())
    print_index()
    print(search_index("hello"))
    print(search_index("charlie"))
    print(search_index("bravo"))
    
    

if __name__ == '__main__':
    main()