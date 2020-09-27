import mysql.connector
from difflib import get_close_matches

def word_check(word, cursor):
    try:
        query = "SELECT Expression FROM Dictionary"
        cursor.execute(query)
        res = [key[0] for key in cursor.fetchall()]
        new_words = get_close_matches(word, res)
        if new_words: return new_words[0]
    except Exception as err:
        print("[!] ERROR : " + str(err))
        return

def query(word, cursor):
    try:
        q = "SELECT * FROM Dictionary WHERE Expression LIKE '" + word +"'"
        cursor.execute(q)
        results = cursor.fetchall()
        if results:
            return results
    except Exception as err:
        print("[!] ERROR : " + str(err))
        return

if __name__ == "__main__":
    try:
        con = mysql.connector.connect(user="ardit700_student", password="ardit700_student",
                                      host="108.167.140.122", database="ardit700_pm1database")
    except Exception as err:
        print("[!] ERROR : " + str(err))
    cursor = con.cursor()
    word = input("Enter Word : ")
    results = query(word, cursor)
    if results:
        for result in results:
            print(result[1])
    else:
        new_word = word_check(word, cursor)
        yn = input(f" Do you mean {new_word}, Press Y for yes / N for no : ")
        if yn.lower() == "y":
            res = query(new_word, cursor)
            if res:
                for r in res:
                    print(r[1])
            else:
                print(f"{word} not found, Exiting...")
        elif yn.lower() == "n":
            print("[!] Exiting ")
        else:
            print("[!] choice unmatched")