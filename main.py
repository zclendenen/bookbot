def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = individual_character_count(text)
    book_report(word_count, char_count)
    


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
            
def book_report(word_count, char_count):
    char_count_list = []
    def sort_on(dict):
        return dict["count"]
    for char, count in char_count.items():
        if char.isalpha():
            char_count_list.append({
                "char": char,
                "count": count
            })
    char_count_list.sort(reverse=True, key=sort_on)
    print(char_count_list)




main() 