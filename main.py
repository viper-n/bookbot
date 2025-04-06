import sys
from stats import get_book_text, get_num_words, get_char_count, get_char_count_sorted

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    char_count_dict_sorted = get_char_count_sorted(get_char_count(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for character in char_count_dict_sorted:
        print(f"{character['letter']}: {character['count']}")
    print("============= END ===============")
    
main()