def get_book_text(filePath):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()