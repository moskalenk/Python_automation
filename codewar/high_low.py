def high_and_low(numbers):

    tmp = numbers.split(' ')
    l = list(map(int, tmp))


    # res = [int(x) for x in numbers.split(' ')]
    # print(res)


    return '{} {}'.format(max(l), min(l))


r = high_and_low('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6')
print(r)


0, 1-2**64