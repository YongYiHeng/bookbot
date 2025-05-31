from stats import (get_words_count, char_count, char_count_sort)
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_text = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f"Found {get_words_count(book_text)} total words")
    print("--------- Character Count -------")
    char_count_in_order = char_count_sort(char_count(book_text))
    for i in char_count_in_order:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()
