def count_words(text):
    lower_text = text.lower()
    split_text = lower_text.split()
    num_words = len(split_text)
    return num_words

def count_chars(text):

    char_counts = {}

    for char in text:
        char = char.lower()

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
    
def character_counts(char_counts):
    character_list = []
    for char, count in char_counts.items():
        character_list.append({"char": char, "count": count})
    
    character_list.sort(key=lambda x: x["count"], reverse=True)

    return character_list
        

