import trie
import time
import input_processing
import os
import sys
import ID_sentence
import linecache

ID = 0
ID_sentences = list()

def insert_data(root, file_name):
    global ID

    with open(file_name, encoding="utf8") as fp:
        line = fp.readline()
        cnt = 1
       
        while line:
            print(cnt)
            ID_sentences.append(ID_sentence.ID_sentence(file_name, cnt))
            sentence =  line.strip()
            for i in range(len(sentence)):
                root.insert(input_processing.clearing_the_sentence(sentence), i, ID)          
            ID += 1
            line = fp.readline()
            cnt += 1


def main(): 
    t = trie.Trie() 

    for file in os.listdir("c-api"):
        if file.endswith(".txt"):
            insert_data(t, os.path.join("c-api", file))
    input_user = ""
    
    while input_user != "stop":
        print("your input --->", end=' ')
        input_user = input()
        t1 = time.time()
        URL = t.search(input_processing.clearing_the_sentence(input_user))
        i = 0
        if URL:
            for url in URL:
                i += 1
                if url:
                    line = linecache.getline((ID_sentences[url]).routing, (ID_sentences[url]).line)
                    print("----------------------------")
                    print("Sentence routing is: " + (ID_sentences[url]).routing)
                    print("Line of sentence is: " + str((ID_sentences[url]).line))
                    print("[" + str(i) + "] " + line)
                
        print(time.time()-t1)

    
if __name__ == '__main__': 
    main() 
