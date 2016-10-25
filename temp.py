#!/usr/bin/python3.5

import usefull_functions
zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# mail = "folky93@tut.by"
# new_zen = (zen + mail).lower()
# vowels = usefull_functions.vowels_count(new_zen)
#
# symbol = usefull_functions.symbol_slices(zen, 18)
# print(symbol)

# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)
#
#
# my_nums = square_numbers((1, 2, 3, 4, 5))
#
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))


list = (1, 2, 3, 4)
nums = [x*x for x in list]
print(nums)




# tracker = {}
#
# for char in zen:
#     if char in tracker:
#         continue
#     tracker[char] = zen.count(char)
#
# print(tracker)
# print(set(zen)) убирает дубликаты

# Почитать про set

# a = None
# if a > 10:
#     print("hello")
# elif print("hi"):
#     print(a)



# def use_fank(s, *args, **kwargs):
#     print(s)
#     print(args)
#     print(kwargs)
# use_fank("123", "jekdd", 123231, k=100)



# def use_fank(s, *args, **kwargs):
#     print(s)
#     print(args)
#     print(kwargs)
#
# pos_args = {"key": "val", "8":"10"}
# use_fank("123", *pos_args)

# d = {"a": "b", "c":"d"}
# for a in d:
#     print(a + d[a])

# d = {"a": "b", "c":"d"}
# for a in d:
#     print(a)






# litters = {}
# # for char in range(1, len(zen) + 1):
# #     print(str(char) + " " "-" " " + zen[char - 1])
#
#
# for char in zen:
#     if char in litters:
#         continue
#     litters[char] = zen.count(char)
#     print(str(char) + "=" + str(litters[char]))



# def gen():
#     i = 1
#     while True:
#         yield i
#         i += 1
#
# name = "kostya"
# d = (letter: next(a) for letter in name)
# print()

# print(gen())
















