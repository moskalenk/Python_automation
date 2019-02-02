def fact(n):
    # if n == 0:
    #     return 1
    # return n * fact(n-1)

    return 2 if n == 2 else n*fact(n-1)
res = fact(20)
print(res)
