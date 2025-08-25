from stats import word_count, char_count, sorted_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    file_path = "books/frankenstein.txt"

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
main()