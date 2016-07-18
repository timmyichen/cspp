#Detect English module

#To use, type this code:
#   import detectEnglish
#   detectEnglish.is_english(someString) #returns true/false
#(There must be a dictionary.txt file in this directory with
# all english words in it, one per line.  You can download
# this file from http://invpy.com/dictionary.txt)

# a string to hold all uppercase and lowercase letters, 
#   plus spaces, tabs, newlines

LETTERS_AND_SPACE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

def loadDictionary():
    dictionaryFile = open('../drafts/_sources/resource/dictionary.txt') # opens file for reading
    englishWords = {} #create empty dictionary
    for word in dictionaryFile.read().split('\n'): #read file and 
                                                   #  split by line
        englishWords[word] = None # add the word as a key 
                                  #   to the dictionary, no value
    dictionaryFile.close()
    return englishWords

# a dictionary to hold all english words in given dictionary.txt file
ENGLISH_WORDS = loadDictionary()

# function: get_english_count
# purpose: gets the number of words that are found in the given
#   dictionary file
# arguments:
#   message: the message to count
# returns:
#   the number of "English" words in the message
def get_english_count(message):
    
    count = 0    
    for word in message:
        if word in ENGLISH_WORDS:
            count+=1
    
    return count

# function: remove_non_letters
# purpose: removes any character that is not a letter or a space
#   from a string
# arguments:
#   message: the message in which to remove non-letter/space chars
# returns:
#   the modified message that no longer contains special chars
def remove_non_letters(message):
    new_message = ""
    for ch in message:
        if ch in LETTERS_AND_SPACE:
            new_message += ch
    return new_message

def message_to_upperlist(message):
    message = remove_non_letters(message.upper())
    m = message.split(" ")
    
    while "" in m:
        m.remove("")
    
    return m

# function: is_english
# purpose: determines whether a message is english based on
#   the percentage of its words that are found in our
#   provided dictionary file
# arguments:
#   message: the message to be analyzed
#   target_percentage: the minimum percentage for message to be
#       considered English. Default value if not provided is 30%
# returns:
#   True if the actual percentage is greater to or equal to the
#       target_percentage
#   False otherwise
def is_english(message, target_percentage=.3):
    message = message_to_upperlist(message)
    total_count = len(message)
    eng_count = get_english_count(message)
    if total_count == 0:
        return False
    actual_percentage = eng_count / total_count
    return actual_percentage > target_percentage