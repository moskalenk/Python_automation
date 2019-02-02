def count_positives_sum_negatives(arr):
    pos, neg = 0, 0

    if len(arr) == 0 or arr == 0:
        return list()
    else:
        p = [el for el in arr if el > 0]


        for el in arr:
            if el > 0:
                pos+=el
            else:
                neg+=el
    return [pos, neg]

count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])