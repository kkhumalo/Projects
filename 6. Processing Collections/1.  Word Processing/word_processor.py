
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """
    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """splits text and returns as split lowercased list:new_text"""
    new_text = split(',?. ', text)
    new_text = [i.lower() for i in new_text]
    new_text = list(filter(None, new_text))   
    return new_text
    

def words_longer_than(length, text):
    """Filters thru txt words length and returns words that consists of 10 letters and more"""
    txt = convert_to_word_list(text)
    words_list = []
    if len(txt) == 0:
        return word_list
    else:
        words_list = list(filter(lambda x: len(x) >= length, txt))  #it filters a list based on the number of char in which are in the list
        return words_list


def words_lengths_map(text):
    """counts the length of each word that is on txt and how many times it appeared."""
    txt = convert_to_word_list(text)
    words_list = dict()
    if len(txt) == 0:
        return words_list
    else:
        filtered_list = list(map(lambda x: len(x), txt))
        words_list = dict((x,filtered_list.count(x)) for x in set(filtered_list))
        return words_list


def letters_count_map(text):
    """counts letters in the list new_txt and it returns each letter and how many times it appeared."""
    txt = split(['', '?', '.', ','], text)
    new_txt = [i.lower() for i in txt]
    letters_list =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if len(txt) == 0:
        return {}
    else:
        letters_count = {key: len([i for i in new_txt if i == key]) for key in letters_list}
    return letters_count


def most_used_character(text):
    """compares indexes until it finds the index that is greater than the previous index and it returns the greatest index"""
    from functools import reduce
    used_char_dictionary = letters_count_map(text)
    popular_char = reduce(lambda a, b: a if used_char_dictionary[a] > used_char_dictionary[b] else b, used_char_dictionary) 
    if not text:
        return None
    return popular_char


if __name__ == "__main__":
    text = 'These are indeed interesting, an obvious understatement, times. What say you?'
    convert_to_word_list(text)
    words_longer_than(10, text)
    words_lengths_map(text)
    letters_count_map(text)
    most_used_character(text)
