import chars_data

def clearing_the_sentence(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(',', '')
    count = 0
    flag = False

    for i in range(len(sentence)):
        
        if sentence[i-count] not in chars_data.chars.keys():
            len_centence = len(sentence)
            sentence = sentence.replace(sentence[i-count], '')
            num = len_centence - len(sentence)
            count += num

        elif sentence[i-count] == ' ':
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
