from chars_data import chars


class TrieNode: 

    def __init__(self): 
        self.children = [None]*69
        self.isEndOfWord = False
        self.URL = set()
        self.pre_URL = set()
  

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

            if index == 0 and len(pCrawl.pre_URL) < 5:
                pCrawl.pre_URL.add(ID)

                if pCrawl.URL:
                    pCrawl.URL.pop()

            elif len(pCrawl.URL) + len(pCrawl.pre_URL) < 5:
                pCrawl.URL.add(ID)

        pCrawl.isEndOfWord = True
  
    def search(self, sentence): 
        return rec_search(self.root, sentence, False, 0)


def rec_search(node, sentence, flag, index):
    res = set()
    
    if index == len(sentence):
        return (node.pre_URL).union(node.URL)
    next_node = node.children[chars[sentence[index]]]
     
    if next_node:
        new_res = rec_search(next_node,sentence ,flag , index+1)

        if new_res:

            if len(new_res) + len(res) > 5:
                res = res.union(set(list(new_res)[:5 - len(new_res)]))

            else:
                res = res.union(new_res)

        if 5 == len(res):
            return res

    if not flag:

        for char in chars.keys():

            if char != sentence[index]:
                new_sentence = sentence[:index] +  char + sentence[index+1:]
                new_res = rec_search(node,new_sentence, True, index)
                
                if new_res:
                    
                    if len(new_res) + len(res) > 5:
                        res = res.union(set(list(new_res)[:5 - len(new_res)]))
                    
                    else:
                        res = res.union(new_res)
            
                if 5 == len(res):
                    return res

    return res
