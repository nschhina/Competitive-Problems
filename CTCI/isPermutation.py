def isPermutation(str1,str2):
    if len(str1)!=len(str2):
        return false
    whatletters=dict()
    for s in str1:
        whatletters[s]+= 1
    for s in str2:
        if s not in whatletters:
            return false
        whatletters[s]-=1
        if whatletters[s]==0:
            del whatletters[s]
    return len(whatletters)==0
