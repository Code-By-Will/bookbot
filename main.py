from stats import get_num_words

def get_book_text(filePath):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents

def main():
    num_words = get_num_words(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()