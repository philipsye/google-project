from chars_data import chars


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
  
    def insert(self,sentence, index=0): 

        pCrawl = self.root
        for level in sentence[index:]: 

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

