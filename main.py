from stats import *
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents

def gen_report(filePath):
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
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filePath = argv[1]
        print(gen_report(filePath))
main()