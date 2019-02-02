# def solve(arr):
#     i = 0
#     d = {}
#     for el in arr:
#         if el not in d:
#             d.update({el: i})
#
#         elif el in d:
#             d[el] = i
#
#         i += 1
#
#     sort = sorted(d.items(), key=lambda x: x[1])
#
#     res = [e[0] for e in sort]
#     return res

def solve(arr):
   b = dict.fromkeys(arr[::-1])
   a = list(b)[::-1]
   return a

solve([3,4,4,3,6,3])