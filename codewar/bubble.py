def bubble(lst):
    for c in range(len(lst) - 1):
        cur_pos = 0
        for el in lst:
            try:
                next_el = lst[cur_pos + 1]
                if el > next_el:
                    tmp = el
                    el = next_el
                    lst[cur_pos] = el
                    lst[cur_pos + 1] = tmp
                cur_pos += 1
            except IndexError:
                continue

    print(lst)


bubble([5, 1, 4, 2, 3, 9, 7, 8, 6])
