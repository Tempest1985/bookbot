import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

from stats import character_counts, count_chars, count_words

def main():

    with open(path) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_counts = count_chars(file_contents)
    sorted_characters = character_counts(char_counts)
    for item in sorted_characters:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")


main()