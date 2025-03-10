# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

This program takes a file path to a .txt file (presumable the text of a book) and outputs a data analysis report.
To run this program, format the command like this: python3 main.py <"file_path_to_the_text_you_want_to_analyze">
This report contains the total number of words in the text, as well as the count of each individual character.
    The data is formatted in character : character_count pairs, each on a new line.

    Example Output (Using the text "Example Output")
    ============ BOOKBOT ============
    Analyzing book found at <"filePath">
    ----------- Word Count ----------
    Found 2 total words
    --------- Character Count -------
    e: 2
    p: 2
    t: 2
    x: 1
    a: 1
    m: 1
    l: 1
    o: 1
    u: 1
    ============= END ===============

    NOTE: You must provide a file path for the code to find the text file!