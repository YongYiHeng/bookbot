def get_words_count(book_text):
    text_list = book_text.split()
    return len(text_list)

def char_count(book_text):
    text_lower = book_text.lower()
    char_dict = {}
    for char in text_lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_function(e):
     return e["num"]

def char_count_sort(char_dict):
    char_count_list = []
    for i in char_dict:
        char_count_list.append({"char": i, "num": char_dict[i]})
    char_count_list.sort(key=sort_function, reverse=True)
    return char_count_list

