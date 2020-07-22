from chars_data import chars


class TrieNode: 

    def __init__(self): 
        self.children = [None]*69
        self.isEndOfWord = False
        self.URL = list()
  
class Trie: 
      
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self):  
        return TrieNode() 
  
    def insert(self,sentence, index, ID): 

        pCrawl = self.root
        for level in sentence[index:]: 

            if not pCrawl.children[chars[level]]: 
                pCrawl.children[chars[level]] = self.getNode() 
            pCrawl = pCrawl.children[chars[level]]
            if len(pCrawl.URL) < 5:
                pCrawl.URL.append(ID)
#           for i in range(5):
#               if pCrawl.URL[i] == None:
# לשנות לכתובת של המשפט
#                 pCrawl.URL[i] = sentence
#                 break
            
        pCrawl.isEndOfWord = True
  
    def search(self, sentence): 
        return rec_search(self.root, sentence, False, 0)
#        pCrawl = self.root 
#        for level in sentence: 
#            pCrawl = pCrawl.children[chars[level]] 
#            if pCrawl == None:
#                return None

#        return pCrawl.URL


def rec_search(node, sentence, flag, index):
    res = list()
    
    if index == len(sentence):
        return node.URL
    next_node = node.children[chars[sentence[index]]]
     
    if next_node:
#אולי אפשר למחוק את הסלייס
        res += rec_search(next_node,sentence ,flag , index+1)
        if 5 == len(res):
            return res

    if not flag:

        for char in chars.keys():
            if char != sentence[index]:
#                new_sentence = sentence[:]
                new_sentence = sentence[:index] +  char + sentence[index+1:]
                res += rec_search(node,new_sentence, True, index)
                if 5 == len(res):
                    return res
    else:
        return res
