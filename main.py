from stats import *

def get_book_text(filePath):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents

def gen_report(filePath):
    bookText = get_book_text(filePath)
    report = "============ BOOKBOT ============\n"
    report +="Analyzing book found at books/frankenstein.txt...\n"
    report +="----------- Word Count ----------\n"
    report +="Found "
    report += str(get_num_words(bookText)) 
    report += " total words\n"
    report += "--------- Character Count -------\n"
    charDict = count_characters(bookText)
    charDictList = sort_lettersDict(charDict)
    for dictList in charDictList:
        if dictList["char"].isalpha():
            report += dictList["char"]
            report += ": "
            report += str(dictList["count"])
            report += "\n"
    '''
    for char in charDict:
        if char.isalpha():
            report += char
            report += ": "
            report += str(charDict[char])
            report += "\n"
    '''
    report += "============= END ==============="
    return report

def main():
    frankFilePath = "./books/frankenstein.txt"
    print(gen_report(frankFilePath))
main()