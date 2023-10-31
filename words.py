# str_list = ["hello", "hey", "yo", "yes"]
# converted_list = [x.upper() for x in str_list]
# print(converted_list)


def return_upper_words(str_list):
    """converts a list of strings to uppercase"""

    converted_list = [i.upper() for i in str_list]
    return converted_list


def return_starts_with(str_list):
    """prints a new string of words in uppercase that begin with hard-coded designated letters"""

    for str in str_list:
        if str.startswith("e") or str.startswith("E"):
            print(str.upper())


def return_upper_words2(str_list, must_start_with):
    """prints a new string of words in uppercase that begin with any designated letters"""

    for str in str_list:
        for letter in must_start_with:
            if str.startswith(letter):
                print(str.upper())
