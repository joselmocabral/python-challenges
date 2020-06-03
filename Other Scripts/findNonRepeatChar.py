def first_non_repeating_letter(string):
    iterable = string.lower()
    print(iterable)
    while len(iterable) > 1:
        if iterable[1:].find(iterable[0]) != -1:
            iterable = iterable.replace(iterable[0], "")
        else:
            break
    if iterable == "":
        return ''
    elif string.find(iterable[0].lower()) != -1:
        return string[string.index(iterable[0].lower())]
    else:
        return iterable[0].upper()