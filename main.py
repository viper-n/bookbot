from stats import get_book_text, get_num_words, get_char_count, get_char_count_sorted
import sys
import os

# Define a safe directory where books are stored
SAFE_BASE_DIR = os.path.abspath("books")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Join the input path to the safe base directory
    requested_path = os.path.abspath(os.path.join(SAFE_BASE_DIR, sys.argv[1]))

    # Check if the resolved path is still inside the safe base directory
    if not requested_path.startswith(SAFE_BASE_DIR):
        print("Error: Invalid file path.")
        sys.exit(1)

    if not os.path.isfile(requested_path):
        print("Error: File does not exist.")
        sys.exit(1)

    text = get_book_text(requested_path)
    char_count_dict_sorted = get_char_count_sorted(get_char_count(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {requested_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for character in char_count_dict_sorted:
        print(f"{character['letter']}: {character['count']}")
    print("============= END ===============")

main()
