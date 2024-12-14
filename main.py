def get_text(file_path: str):
    with open(file_path) as f:
        return f.read()  

def count_word(text: str): 
    return len(text.split())

def count_char_occurences(text: str): 
    result = {}
    text_lc = text.lower()
    for char in text_lc:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def sort_on(list_to_sort):
    return list_to_sort["num"]

def dict_to_list(dict_to_sort):
    result = []
    for key, value in dict_to_sort.items():
        result.append({"char": key, "num": value})
    return result


def print_report(file_path: str):
    text = get_text(path_to_text)
    word_count = count_word(text)
    char_occurences = count_char_occurences(text)
    print(f"--- Begin report of {file_path} ---")
    print (f"{word_count} words found in the document")
    print()

    char_occ_list = dict_to_list(char_occurences)

    char_occ_list.sort(reverse=True, key=sort_on)
    for char_dict in char_occ_list:
        char = char_dict['char']
        if char.isalpha():
            occ = char_dict['num']
            print(f"The '{char}' character was found {occ} times")
    
    print ('--- End report ---')

if __name__ == '__main__':
    path_to_text = "books/frankenstein.txt"
    print_report(path_to_text)
    
