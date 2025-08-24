from stats import word_count, char_count#, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    count = word_count(get_book_text("books/frankenstein.txt"))
    print(f"{count} words found in the document")
    chars = char_count(get_book_text("books/frankenstein.txt"))
    for char in chars:
        print(f"'{char}': {chars[char]}")
main()