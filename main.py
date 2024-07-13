def main():
    book_path = "books/frankenstein.txt"
    words = get_book_text(book_path)
    word_count = count_words(words)
    characters = count_characters(words)
    sorted_characters = create_characters_list(characters)
    
    print(f"{word_count} words were found in the document")
    for c in sorted_characters:
        print(f"The character '{c["char"]}' was found {c["count"]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)

def count_characters(words):
    lowered_string = words.lower()
    letters = {}
    for letter in lowered_string:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def create_characters_list(dict):
    list = []
    for item in dict:
        if item.isalpha():
            list.append({"char": item, "count": dict[item]})
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["count"]

main()