import sys
from stats import calculate_number_of_words, calculate_number_of_chars, sort_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    total_chars = calculate_number_of_chars(text)
    sorted_list = sort_dict(total_chars)

    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {sys.argv[1]}...\n"
        "----------- Word Count ----------\n"
        f"Found {calculate_number_of_words(text)} total words\n"
        "--------- Character Count -------"
    )
    for item in sorted_list:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")


main()
