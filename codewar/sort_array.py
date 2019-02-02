def sort_array(source_array):
    res_array = source_array[:]
    
    d = {item:count for count, item in enumerate(source_array)}
    sd = sorted(d)
    

    for el in sd:

        if el % 2 != 0:
            min_el = min(sd)
            res_array[min_el] = el
            sd.pop(min_el)

    return res_array

sort_array([5,3,2,8,1])