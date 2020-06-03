def dirReduc(arr):
    strDir = '|'.join(arr)
    nxtStr = strDir
    strDir = ''
    while(nxtStr != strDir and nxtStr != ''):
        strDir = nxtStr
        nxtStr = nxtStr.replace('NORTH|SOUTH', '')
        nxtStr = nxtStr.replace('SOUTH|NORTH', '')
        nxtStr = nxtStr.replace('WEST|EAST', '')
        nxtStr = nxtStr.replace('EAST|WEST', '')
        nxtStr = nxtStr.replace('||', '|')
    return list(filter(lambda x: x!='',nxtStr.split('|')))