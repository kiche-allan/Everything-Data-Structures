class TrieNode:
    
    def __init__(self): 
        self.children = {}
        self.is_end_of_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
        
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word
    
    
    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


# In this example, the TrieNode class represents a node in the trie and contains a dictionary of its children nodes and a boolean flag to indicate if it is the end of a word. The Trie class is the main class that represents the trie and provides methods to insert, search, and search for prefixes in the trie.

# The insert method inserts a word into the trie by traversing the trie from the root node and creating new nodes as needed for each character in the word. The search method searches for a word in the trie by traversing the trie from the root node and checking if the final node is marked as the end of a word. The starts_with method searches for prefixes in the trie by traversing the trie from the root node and checking if all the characters in the prefix exist in the trie.

# Tries, also known as prefix trees or digital trees, are often used in algorithms and computer science to efficiently store and search for strings. Here are some common algorithms that use tries:

# Autocomplete: Autocomplete is a feature in many applications that suggests words or phrases based on what the user has typed so far. A trie can be used to store a large set of words, and as the user types each character, the trie can be traversed to find all the words that start with the current prefix.

# Spell checking: A trie can also be used to check if a word is spelled correctly. By traversing the trie to find each character in the word, it can be determined if the word is a valid word in the trie or not.

# Longest common prefix: Given a set of strings, a trie can be used to find the longest common prefix of all the strings. By traversing the trie and finding the point where the first character differs between any two strings, the longest common prefix can be found.

# Text compression: Tries can be used in text compression algorithms, such as the Lempel-Ziv-Welch (LZW) algorithm. The LZW algorithm uses a trie to store a dictionary of frequently occurring substrings, and replaces these substrings with codes to compress the text.

# Word frequency counting: A trie can be used to count the frequency of words in a set of text. By inserting each word into the trie and incrementing a count value at the end of the word, the frequency of each word can be determined by traversing the trie.

# These are just a few examples of how tries can be used in algorithms. Tries are a powerful data structure that can be used in many applications that involve searching and storing strings.

# Properties

# It is typically used to store or search strings in space and time efficient manner.
# Any node in trie can store non repetetive multiple characters
# Every node stores link of the next charater in the string
# Every node keeps track of 'end of string'