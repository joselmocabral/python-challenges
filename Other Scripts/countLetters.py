#See if a string out of order can fit in another

def scramble(s1, s2):
    for l in set(s2):
        if s1.count(l) < s2.count(l):
            return False
    return True
