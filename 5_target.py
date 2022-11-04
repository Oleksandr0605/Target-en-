from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    ret_lst = []
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(chr(random.randint(65, 90)))
        ret_lst.append(temp)
    return ret_lst




def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f) as fff:
        fff.readline()
        fff.readline()
        fff.readline()
        a = fff.readlines()
    a = [el.strip() for el in a]
    # lst1 = [el.strip for el in a if el[-1] == '\n']
    # Довжина слова >= 4
    # Перевірити чи центральна буква з леттерс є в списку
    # Кожна літера може зустрічатися у слові стільки разів, скільки разів вона 
    # зустрічається на ігровому полі
    return a



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    ret = []
    while a := input():
        ret.append(a)
    return ret


def get_pure_user_words(user_words: List[str], letters: List[str],\
words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    used_letters = []
    temp_lst = []
    lst_dict_letters = []
    lst_dict_letters_user = []
    for elm in letters:
        if elm not in used_letters:
            lst_dict_letters.append((elm, letters.count(elm)))
            used_letters.append(elm)
    for word in user_words:
        temp_lst = []
        used_letters = []
        for elm in word:
            if elm not in used_letters:
                temp_lst.append((elm, word.count(elm)))
                used_letters.append(elm)
        lst_dict_letters_user.append(temp_lst)
    
    return lst_dict_letters_user

    

# print(get_words('C:\YKY\OP\Python\Lab\L_06\en.txt', ['a', 'b']))
# print(generate_grid())
# print(get_user_words())
print(get_pure_user_words(get_user_words(), 'aasssrtttt', []))

def results():
    pass