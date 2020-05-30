#convert alphabet string to alphabet position

def alphabet_position(text):
    if(text.isalpha()):
        text = ' '.join([str(ord(n.lower())-ord('a')+1) for n in text])
    else:
        text = ''
    return text
