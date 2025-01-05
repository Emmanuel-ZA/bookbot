def words(book):
    num_words = 0
    words = book.split()
    return len(words)

def characters(book):
    lowered_book = book.lower()
    characters={"a" : 0,
                "b" : 0,
                "c" : 0,
                "d" : 0,
                "e" : 0,
                "f" : 0,
                "g" : 0,
                "h" : 0,
                "i" : 0,
                "j" : 0,
                "k" : 0,
                "l" : 0,
                "m" : 0,
                "n" : 0,
                "o" : 0,
                "p" : 0,
                "q" : 0,
                "r" : 0,
                "s" : 0,
                "t" : 0,
                "u" : 0,
                "v" : 0,
                "w" : 0,
                "x" : 0,
                "y" : 0,
                "z" : 0}

    for char in lowered_book:
        if char in characters: 
            characters[char] += 1 
    
    return characters

def sort_on(dict):
    return dict["count"]

def character_lists(characters):
    character_list = []

    for char, count in characters.items():
        char_dict = {"character" : char, "count" : count}
        character_list.append(char_dict)

    return character_list    


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = words(file_contents)
    num_characters = characters(file_contents)

    num_character_list = character_lists(num_characters)
    num_character_list.sort(reverse=True, key=sort_on)
    

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for char_dict in num_character_list:
        character = char_dict["character"]
        count = char_dict["count"]
        print(f"The '{character}' character was found {count} times")

    print("--- End report ---")
    
if __name__ == "__main__":
    main()





    
