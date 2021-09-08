"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #iterate through the text file and concat each line as a string to the previous string
    
    contents = open(file_path).read() #opens entire file
    
    return contents #'Contents of your file as one long string'
print(open_and_read_file('green-eggs.txt'))



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
    #split up the string into pairs of words that overlap
    #then iterate through each pair (do we use dictionary.get())
    #so each two words are the key and the value is a list of all possible following words
    # your code goes here

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
