import json
from difflib import get_close_matches

data = json.load(open("data/dictionary.json"))


def retrieve_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        # return data[close_match]
        return "Did you mean this instead? %s : %s " % (close_match , data[close_match])
    else:
        return "Word does not exist in the dictionary"


user_word = input("Word: ")
output = retrieve_definition(user_word)

if type(output) == list:
    for item in output:
        print("-", item)
else:
    print(output)