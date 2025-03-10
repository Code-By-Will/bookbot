def get_num_words(bookText): #A function that gets how many words there are in the provided text
    wordsList = bookText.split() #We want to take advantage of the len() list function, so we split the text into a list of words
    return len(wordsList) 

def count_characters(bookText):
    '''
    With this function we want to accomplish the following:
        1. take the raw text provided, and loop over the letters
        2. create a dictionary of key : value pairs - character : how_many_times_that_character_appears
        3. return that dictionary    
    '''
    lettersDict = {} #This is what we will output at the end of the function
    #1:
    for c in bookText:
        c_lower = c.lower() #We don't care about case for this
        
        #2:
        '''
            - If character already exists in dictionary, increment count
            - Otherwise, add it with count of 1
        '''
        if c_lower in lettersDict:
            lettersDict[c_lower] += 1
        else:
            lettersDict[c_lower] = 1
    #3:
    return lettersDict

def sort_by_count(charDict): #Helper function for the .sort() method we use in sort_lettersDict()
    return charDict["count"]

def sort_lettersDict(lettersDict):
    '''
    In order to best format our data we need to do a few things:
        1. We need a list of dictionaries in order to use the .sort() method, so we need to create one in the proper formatting
            using the data from the dictionary we created with the count_characters() function
        2. Use the .sort() method to organize and sort the data by the number of times the letter was used in the text
    '''
    lettersDictList = []
    #1:
    for k in lettersDict: #loop over the provided dictionary, using k to store the key for each step of the program
        char = k
        count = lettersDict[k]
        lettersDictList.append({"char" : char, "count" : count})#Creates a dictionary, and appends it to a list
    #2:
    lettersDictList.sort(reverse = True, key=sort_by_count) #Actually sorting the data! (using the .sort() method)

    return lettersDictList #returning the final product