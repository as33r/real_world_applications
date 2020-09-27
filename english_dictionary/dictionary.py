import json
from difflib import get_close_matches

def translate(data, word):
    match = get_close_matches(word, data.keys())
    if word in data:
        return data[word]
    elif len(match) > 0:
        yn = input(f"Do you mean {match[0]}, Y/N ")
        if yn.lower() == "y":
            return data[match[0]]
        elif yn.lower() == "n":
            return f"'{word}' is not in our database yet, please try another"
        else:
            return "We didn't understand your choice"
    else:
        return f"'{word}' is not in our database yet, please try another"

if __name__ == "__main__":
    word = input("Enter word : ")
    filename = "data.json"
    with open(filename, "r") as file:
        data = json.loads(file.read())
    result = translate(data, word.lower())
    if type(result) == list:
        for item in result:
            print(item)
    else:
        print(result)