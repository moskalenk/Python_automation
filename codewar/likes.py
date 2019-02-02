def likes(names):
    n = len(names)
    d = {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }
    t = d[min(4, n)]
    res = t.format(*names[:3], others=n-2)
    print(res)

likes(['Kostya', 'Kate', 'Egor'])