def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = individual_character_count(text)
    print(char_count)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count


def individual_character_count(text):
    character_count = {}
    for character in text:
        lower = character.lower()
        if lower not in character_count:
            character_count[lower] = 1
        else:
            character_count[lower] += 1
    return character_count
            




main()