import json

data = json.load(open("data.json"))

def enter_word():
    word = input("Enter word: ")
    print(translate(word))
    return word

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please double check it."

if __name__ == '__main__':
    w = enter_word()
    translate(w)
