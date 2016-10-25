#!/usr/bin/python3.5
# coding:utf-8

import this

zen = str(this)
mail = "folky93@mail.ru"
new_zen = mail + zen
print(len(new_zen))

vowels = set("aeiouy")

count = str(None)
for litter in zen:
    if litter.lower() in vowels:
        count += 1

pos = 18
for letter in new_zen [17::18]:
    pos += 18
    if letter == "\n":
        letter = "NEW LINE DETECTED"
    print(letter.swapcase() + str(pos))

print(count)

# print(new_zen)