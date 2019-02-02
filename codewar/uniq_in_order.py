from itertools import groupby

def unique_in_order(iterable):
    # temp = None
    # res = []
    #
    # for i in iterable:
    #     if i != temp:
    #         res.append(i)
    #         temp = i
    #
    # print(res)
    # return res


    for k in groupby(iterable):
        print(k)
        print(_)
        pass


    return  [k for (k, _) in groupby(iterable)]



# unique_in_order('AAAABBBCCDAABBB')


groups = []
uniquekeys = []

data = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("animal", "speed boat")]

for k, _ in groupby(data, lambda x: x[0]):
   uniquekeys.append(k)
   groups.append(_)

print(groups)
print(uniquekeys)