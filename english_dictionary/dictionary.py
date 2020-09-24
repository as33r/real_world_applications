import json
from difflib import get_close_matches

def translate(data, word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return get_close_matches(word, data.keys())
    else:
        return

if __name__ == "__main__":
    word = input("Enter word : ")
    filename = "data.json"
    with open(filename, "r") as file:
        data = json.loads(file.read())
    result = translate(data, word.lower())
    if result:
        for item in result:
            print(item)
    else:
        print(f"'{word}' is not in our database yet, please try another")