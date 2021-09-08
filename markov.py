"""Generate Markov text from text files."""

from random import choice
contents = open("green-eggs.txt").read() #opens entire file

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #iterate through the text file and concat each line as a string to the previous string
    
    return contents #'Contents of your file as one long string'
#print(open_and_read_file('green-eggs.txt'))



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    #takes long content string and makes a word list
    words = contents.split()
    print("words = ", words)
    
    #split up the string into pairs of words that overlap
    for i in range(len(words)-1):#loop over every two pair of words in contents
        #add each tuple as a key in our dictionary
        key = (words[i], words[i+1])
        value = []
        chains[key] = value
       
        #is this key alrady in my dict
        #if yes, append to the list instead of creating a new list
    print("line 57=", chains)
    for i in range (len(words)-2):
        #print("inside of i in range len(chains-2)")
        chains[key] = chains.get(key, [])
        # print("These words we want to add as values: ", words[i + 2])
        chains[key].append(words[i+2])
        
    #so each two words are the key and the value is a list of all possible following words
    print("This is chains: ", chains)

    return chains

def make_text(chains):
    """Return text from chains."""

    words = []
    # let random pick next words based on the key tuple
    # output some possible completed lines
    # return the joined words (completed lines)


    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
