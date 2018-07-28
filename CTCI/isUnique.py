def isUnique(word_str):
    word_dict= dict()
    for s in word_str:
        if s in word_dict:
            return false
        word_dict[s]=s
    return true
