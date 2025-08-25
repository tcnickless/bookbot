def sort_on(items):
    return items["num"]

def word_count(text):
    return len(text.split())

def char_count(text):
    counts = {}
    for letter in text:
        letter = letter.lower()
        if letter not in counts:
            counts[letter] = 1
        elif letter in counts:
            counts[letter] += 1
    return counts

def sorted_char_count(char_dict):
    sorted_list = []
    for entry in char_dict:
        sorted_list.append({"char" : entry, "num" : char_dict[entry]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list