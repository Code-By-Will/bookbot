def get_num_words(bookText):
    wordsList = bookText.split()
    return len(wordsList)

def count_characters(bookText):
    lettersDict = {}
    for c in bookText:
        c_lower = c.lower()
        # If character already exists in dictionary, increment count
        # Otherwise, add it with count of 1
        if c_lower in lettersDict:
            lettersDict[c_lower] += 1
        else:
            lettersDict[c_lower] = 1
    return lettersDict