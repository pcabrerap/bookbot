def calculate_number_of_words(text):
    return len(text.split())


def calculate_number_of_chars(text):
    updated_text = text.lower()
    total_chars = {}

    for item in updated_text:
        count = total_chars.get(item) + 1 if total_chars.get(item) else 1
        total_chars[item] = count

    return total_chars


def sort_on(dict):
    return dict["count"]


def sort_dict(total_chars):
    sorted_list = []
    for letter, count in total_chars.items():
        sorted_list.append({"character": letter, "count": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
