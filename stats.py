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