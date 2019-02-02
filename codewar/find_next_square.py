from math import sqrt


def find_next_square(sq):
    current_sqrt = sqrt(sq)

    if current_sqrt - int(current_sqrt) == 0:
        return int((current_sqrt + 1) ** 2)
    else:
        return -1

# a = find_next_square(15241383936)
# print(a)


n = 14 ** 0.5
print(n)

print(n.is_integer())