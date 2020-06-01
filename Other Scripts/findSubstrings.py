def in_array(array1, array2):
    resp = []
    a2 = array2.copy()
    for elem1 in array1:
        for elem2 in a2:
            if(elem2.find(elem1) != -1):
                resp.append(elem1)
                break
    return list(dict.fromkeys(sorted(resp)))