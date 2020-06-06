def min_bigger(n_str_res, n):
    return min(list(filter(lambda x: x > n, n_str_res)))
    
def next_bigger(n):
    n_str = list(reversed(list(map(lambda x: int(x), list(str(n))))))
    change = False
    for y in range(0, len(n_str) - 1):
        if n_str[y] > n_str[y+1]:
            position = n_str[:y+1].index(min_bigger(n_str[:y+1], n_str[y+1]))
            n_str[position], n_str[y+1] = n_str[y+1], n_str[position]
            n_str[:y+1] = sorted(n_str[:y+1], reverse = True)
            change = True
            break
    if change:
        n_str = list(reversed(list(map(lambda y: str(y), n_str))))
        return int(''.join(n_str))
    else:
        return -1
    