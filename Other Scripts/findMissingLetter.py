def find_missing_letter(chars):
    for x in range(0,len(chars)-1):
        if(ord(chars[x+1]) - ord(chars[x]) == 2):
            return chr(ord(chars[x])+1)

