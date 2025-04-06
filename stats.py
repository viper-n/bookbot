def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_char_count_sorted(char_count_dict):
    char_count_dict_sorted = []
    for key, value in char_count_dict.items():
        if key.isalpha():
            character = {}
            character["letter"] = key
            character["count"] = value
            char_count_dict_sorted.append(character)
    char_count_dict_sorted.sort(reverse = True, key = lambda x: x["count"])

    return char_count_dict_sorted