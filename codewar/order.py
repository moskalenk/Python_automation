def order(sentence):
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    ss = sentence.split(' ')
    res = []
    for n in num:
        for el in ss:
            if n in el:
                res.append(el)

    return ' '.join(res)

# r = order("is2 Thi1s T4est 3a")
# print(r)


def extract_number(word):
    for l in word:
        if l.isdigit(): return int(l)
    return None

extract_number("is2 Thi1s T4est 3a")