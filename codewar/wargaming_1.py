def one_zero(seq, n):
    it = 0
    curr = None
    change = 0

    for el in seq:
        if it <= n:

            if el != curr:
                change += 1
                curr = el
                it += 1
            else:
                it += 1
                continue

        else:
            break

    if change % 2 == 0:
        return 0
    else:
        return 1

res = one_zero('1001110000111110000001111111', 5)
print(res)