def sort_array(source_array):
    res_array = source_array[:]
    
    d = {item:count for count, item in enumerate(source_array)}
    sd = sorted(d)
    
    for el in sd:
        if el % 2 != 0:
            i = d[el]
            res_array[i] = el
    print(res_array)  
    return res_array