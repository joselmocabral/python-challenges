def valid_parentheses(string):
    string = ''.join(list(filter(lambda s: s=="(" or s ==")", string)))
    while (string.find("()") != -1 and string != ''):
        string = string.replace("()", "")
    return string == ""