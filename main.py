import trie
import time
import input_processing


def main(): 
  
    # Input keys (use only 'a' through 'z' and lower case) 
    setences = ["It *is* possible in some cases to change an object's type under certain controlled conditions. It generally isn't a good idea though since it can lead to some very strange behaviour if it is handled incorrectly",
                "The \"hash()\" \"iter()\" \"reversed()\" and \"contains()\" methods have special handling for this; others will still raise a \"TypeError\" but may do so by relying on the behavior that \"None\" is not callable.",
                "The \"hash()\" \"iter()\" \"reversed()\"",
                "The \"hash()\" \"iter()\" \"reversed()\" and \"contain()\" methods have special handling for this; others will still raise a \"TypeError\" callable."
    ] 

    t = trie.Trie() 
    for setence in setences: 
        for i in range(len(setence)):
            t.insert(input_processing.clearing_the_sentence(setence), i)

    t1 = time.time()
    URL = t.search(input_processing.clearing_the_sentence("hash()\" \""))
    for url in URL:
        if url:
            print(url)
    print(time.time()-t1)


if __name__ == '__main__': 
    main() 
