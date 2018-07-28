def palindromic(string):
    letters = dict()
    count = 0
    for s in string:
        letters[s]+=1
    for key in letters:
        if (letters[key]%2)==1:
            count+=1
    if count <=1:
        return true
    return false
