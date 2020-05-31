#Encoding chars in a string with 13 chars after it

def conv(c):
    if c.isupper():
        n = ord(c) - ord('A')
        n += 13
        print(n)
        n = n - 26 if n >= 26 else n
        return chr(ord('A') + n)
    else:
        n = ord(c) - ord('a')
        n += 13
        n = n - 26 if n >= 26 else n
        return chr(ord('a') + n)


def rot13(message):
    return ''.join([conv(c) if c.isalpha() else c for c in message])
