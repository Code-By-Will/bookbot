from stats import * 
import sys #Importing this mostly for sys.argv so we can take arguments and make the code more versatile

def get_book_text(filePath):
    with open(filePath) as f: #We use 'with' because it means that it will close out of the file after the with block
        fileContents = f.read()
    return fileContents

def gen_report(filePath):
    '''
    This function takes a file path, and generates a report, using multiple different functions to filter and sort data
    The data is the text of a book, the file path of which is given as an argument when running the program
    '''
    bookText = get_book_text(filePath)
    report = "============ BOOKBOT ============\n"
    report +="Analyzing book found at "
    report += filePath
    report += "\n"
    report +="----------- Word Count ----------\n"
    report +="Found "
    report += str(get_num_words(bookText)) 
    report += " total words\n"
    report += "--------- Character Count -------\n"
    '''
    For this information, we need to get the count_characters dictionary, and sort / format it with sort_lettersDict
    Then, we loop over the list of dictionaries, and pull the data we want, in the format we want it to add it to our
        report. 
    We want it to be in the format of the character "char" and the number of times that character appears in the text "count".
    We want it to be in the format of "char: count"
    '''
    charDict = count_characters(bookText)
    charDictList = sort_lettersDict(charDict)
    for dictList in charDictList:
        if dictList["char"].isalpha():
            report += dictList["char"]
            report += ": "
            report += str(dictList["count"])
            report += "\n"
    report += "============= END ==============="
    return report

def main(): 
    argv = sys.argv #Assigning the input to a list variable
    if len(argv) != 2: #We need the name of the python file to run, and the file path to the text we want to use as input
        print("Usage: python3 main.py <path_to_book>") #shows the correct way to use this program
        sys.exit(1) #Gives an exit code of 1 to indicate a failure
    else:
        filePath = argv[1] 
        print(gen_report(filePath)) #prints our generated report using the gen_report() function.
main()