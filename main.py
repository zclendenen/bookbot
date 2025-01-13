def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = individual_character_count(text)
    book_report(book_path, word_count, char_count)
    


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
            
def book_report(book_path, word_count, char_count):
    char_count_list = []
    def sort_on(dict):
        return dict["num"]
    for char, count in char_count.items():
        if char.isalpha():
            char_count_list.append({
                "char": char,
                "num": count
            })
    char_count_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for char_dict in char_count_list:
        print(f"The {char_dict['char']} character was found {char_dict['num']} times")
    print("--- End report ---")




main() 