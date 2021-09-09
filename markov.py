"""Generate Markov text from text files."""

from random import choice
contents = open("short-green-eggs.txt").read() #opens entire file

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
    words1 = contents.split()
    #print("words = ", words)
    
    #split up the string into pairs of words that overlap
    for i in range(len(words1)-1):#loop over every two pair of words in contents
        #add each tuple as a key in our dictionary
        
        key = (words1[i], words1[i+1])
       
        value = []
        chains[key] = value
        print("chains[key]: ", chains[key])
        #print("key list: ", key_list)
        
    #print("Our final dictionary = ", chains) #test
    key_list = []
    for i in range(len(words1)-2): #supposed to start with the word "would"
        #print("inside of i in range len(chains-2)")
        #print("This is the number of iterations to make: " , i)
        key = (words1[i], words1[i + 1])
        chains[key] = chains.get(key, []) #why was this starting with the last key?
        chains[key].append(words1[i+2])
        key_list.append(words1[i])
        key_list.append(words1[i + 1])
        #print("Here's each key and the word we're appending to value list: ", key, words[i+2]) #test that shows we're only evaluating the last key
    print("key list: ", key_list)   
    #so each two words are the key and the value is a list of all possible following words
    #print("This is chains: ", chains)

    return chains, key_list


def make_text(chains):
    """Return text from chains."""

    words = []
    # let random pick next words based on the key tuple
    #make keys into list, then use choice to get a random key
    random_key = choice(key_list)
    #append random key into words list
    #output some possible completed lines
    
    #where the loop starts
    #search for the random key in the dictionary (last two words of the words list)
    #use choice on the value of random key to get a random value
    #append random value to words list
    #start over again using the last two words in words list [-2::-1] as a key to search for
   
    #return the joined words (completed lines)
    return ' '.join(words)


input_path = 'short-green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
