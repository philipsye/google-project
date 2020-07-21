def clearing_the_sentence(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(',', '')
    count = 0
    flag = False

    for i in range(len(sentence)):
        if sentence[i-count] == ' ':
            if flag:
                sentence = sentence[:i-count]+sentence[i-count+1:]
                count += 1
            flag = True
        else:
            flag = False

    if sentence[0] == ' ':
        sentence = sentence[1:]
    
    if sentence[-1] == ' ':
        sentence = sentence[:-1]

    return sentence
