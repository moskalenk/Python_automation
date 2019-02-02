import string

def is_pangram(s):
    # lett = list(string.ascii_lowercase)
    #
    # l_s = s.lower()
    #
    # for s in l_s:
    #     if s in lett:
    #         del lett[lett.index(s)]
    #
    # print(lett)
    # print(l_s)

    # s = s.lower()
    # return set(string.ascii_lowercase).issubset(s.lower())
    for letter in string.ascii_lowercase:
        if letter in s:
            return True
        else:
            return False


    return all(letter in s for letter in string.ascii_lowercase)


res = is_pangram('sdf  and, ya')
print(res)