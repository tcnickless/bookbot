from stats import word_count, char_count, sorted_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    count = word_count(get_book_text(file_path))
    print(f"Found {count} total words")

    print("--------- Character Count -------")
    chars_list = sorted_char_count(char_count(get_book_text(file_path)))
    for entry in chars_list:
        print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")

if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print("Bookbot takes 1 argument. Please provide the file path of the book.")
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)