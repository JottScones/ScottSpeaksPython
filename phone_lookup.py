import re

def word_lookup(word):
    # Returns phones associated with first matching word in dict
    searchfile = open("moby_phones.txt", "r")
    for line in searchfile:
        if line.lower().startswith(word.lower() + " "):
            print('Recognised: [{}]'.format(word))
            searchfile.close()
            return line.split(' ')[1].strip('\n')

    print('Not Recognised: [{}]'.format(word))
    return ''

def sentence_lookup(sentence):
    # Returns array of strings containing phonetic descriptions of each word
    words       = process_sentence(sentence)
    words_pairs = find_word_pairs(words)
    phones      = list(map(word_lookup, words_pairs))
    return phones

def process_sentence(sentence):
    # Remove non alphabet characters and extraneous spaces
    # Returns list of cleaned words
    str_only_alpha   = re.sub('[^A-Za-z -]', '', sentence)
    str_single_space = re.sub(' +', ' ', str_only_alpha)

    words  = str_single_space.split(' ')
    return words

def find_word_pairs(words_arr):
    # Some words in dict appear as word pairs of the form: word1_word2
    # (e.g. homo_sapien)
    # This function tries to find valid pairs and replaces them in words array
    toRemove = []

    for i in range(len(words_arr) - 1):
        local_pair = words_arr[i] + '_' + words_arr[i + 1]

        if (word_lookup(local_pair) != ''):
            unique_id        = str(i + 1)
            words_arr[i]     = local_pair
            words_arr[i + 1] = unique_id

            toRemove.append(unique_id)

    # Filter out the uid of words that have been paired
    new_words_arr = [w for w in words_arr if w not in toRemove]
    return new_words_arr
