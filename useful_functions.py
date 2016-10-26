
import string

# text = ['Airplane','air12port','apple','ball', 'air3284_*gun','airsort','aidoos','aimag']
def vowels_count(text):
    litters = {}
    vowels = ("a", "e", "o", "y", "u", "i")
    for char in text:
        if char in litters:
            continue

        if char in vowels:
            number = text.count(char)
            litters[char] = number
    return litters

def symbol_slices(text, n):
    d = {}
    for char in range(1, len(text) + 1):
        if char % n == 0:
            d[char] = text[char - 1]
    return d


def not_alpha_list(text):
    alpha = []
    for elem in text:
        if not elem.isalpha():
            alpha.append(elem)
    return alpha

def only_alphabet(text):
    correct = []
    for elem in not_alpha_list(text):
        elem = str(elem)
        pars = (x for x in elem if x.isalpha())
        res = "".join(pars)
        correct.append(res)
    return correct

def autocomplete(text, char_slice):
    _list = [elem for elem in text if elem.isalpha() if char_slice in elem]
    for i in only_alphabet(text):
        _list.append(i)
    if len(_list) > 5:
        end_list = _list[0:5]
        return end_list
    else:
        return _list

def TO_WEIRD(str_text):
    str_temp = ""
    for elem in str_text:
        pos_elem = str_text.index(elem)
        if pos_elem % 2 != 0:
            str_temp += elem
            string.capwords(str_temp)
        else:
            up_elem = elem.upper()
            str_temp += up_elem
            string.capwords(str_temp)
    return str_temp

def SUM(number):
    numb = (number)
    temp_numb = 0
    for elem in numb:
        if type(elem) == int:
            temp_numb += elem
    return temp_numb


def SPAM(number):
    return str('egg'*number)
