import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):

    w = w.lower()
    found = get_close_matches(w, data, cutoff=0.8)

    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(found) > 0:
        yn = input("Did you mean {}? Type Y for yes or N for no".format(found[0]))
        if yn == "Y":
            return data[found[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "You didn't enter Y or N"
    else:
        return "The word doesn't exist. Please double check it."

if __name__ == '__main__':
    word = input("Enter word: ")
    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
