from stats import get_num_words
from stats import count_characters

def get_book_text(filePath):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents

def main():
    frankFilePath = "./books/frankenstein.txt"
    num_words = get_num_words(get_book_text(frankFilePath))
    print(f"{num_words} words found in the document")

    numCharacters = count_characters(get_book_text(frankFilePath))
    for char, count in numCharacters.items():
        print(f"'{char}': {count}")

main()