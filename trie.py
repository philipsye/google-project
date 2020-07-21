class TrieNode: 

    def __init__(self): 
        self.children = [None]*67
        self.isEndOfWord = False
        self.URL = [None]*5
  
class Trie: 
      
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self):  
        return TrieNode() 
  
    def insert(self,sentence): 
        pCrawl = self.root  
        for level in sentence: 

            if not pCrawl.children[chars[level]]: 
                pCrawl.children[chars[level]] = self.getNode() 

            for i in range(5):
                if pCrawl.URL[i] == None:
# לשנות לכתובת של המשפט
                    pCrawl.URL[i] = sentence
                    break
            pCrawl = pCrawl.children[chars[level]]
        pCrawl.isEndOfWord = True
  
    def search(self, sentence): 
        pCrawl = self.root 
        for level in sentence: 
            pCrawl = pCrawl.children[chars[level]] 
            if pCrawl == None:
                return None
        return pCrawl.URL


chars = {
    ' ': 0,
    '!': 1,
    '#': 2,
    '$': 3,
    '%': 4,
    '&': 5,
    '*': 6,
    '(': 7,
    ')': 8,
    '_': 9,
    '-': 10,
    '=': 11,
    '+': 12,
    '[': 13,
    ']': 14,
    '{': 15,
    '}': 16,
    '\\': 17,
    '|': 18,
    '/': 19,
    '?': 20,
    '<': 21,
    '>': 22,
    '.': 23,
    ':': 24,
    ';': 25,
    '\'': 26,
    '"': 27,
    '@': 28,
    '^': 29,
    '~': 30,
    '’': 31,
    '0': 32,
    '1': 33,
    '2': 34,
    '3': 35,
    '4': 36,
    '5': 37,
    '6': 38,
    '7': 39,
    '8': 40,
    '9': 41,
    'a': 42,
    'b': 43,
    'c': 44,
    'd': 45,
    'e': 46,
    'f': 47,
    'g': 48,
    'h': 49,
    'i': 50,
    'j': 51,
    'k': 52,
    'l': 53,
    'm': 54,
    'n': 55,
    'o': 56,
    'p': 57,
    'q': 58,
    'r': 59,
    's': 60,
    't': 61,
    'u': 62,
    'v': 63,
    'w': 64,
    'x': 65,
    'y': 66,
    'z': 67,
}


def main(): 
  
    # Input keys (use only 'a' through 'z' and lower case) 
    setences = ["It *is* possible in some cases to change an object's type under certain controlled conditions. It generally isn't a good idea though since it can lead to some very strange behaviour if it is handled incorrectly",
                "The \"hash()\" \"iter()\" \"reversed()\" and \"contains()\" methods have special handling for this; others will still raise a \"TypeError\" but may do so by relying on the behavior that \"None\" is not callable.",
                "The \"hash()\" \"iter()\" \"reversed()\"",
                "The \"hash()\" \"iter()\" \"reversed()\" and \"contain()\" methods have special handling for this; others will still raise a \"TypeError\" callable."
    ] 

    t = Trie() 
    for setence in setences: 
        t.insert(setence.lower())

    URL = t.search("the \"hash()\" \"")
    for url in URL:
        if url:
            print(url)

if __name__ == '__main__': 
    main() 
