# Create a spiral of size using zeros and ones

def spiralize(size):
    i, j = 0, 0
    dir = 0
    spiral = [[0 for col in range(size)] for row in range(size)]
    k = 0
    while (True):
        k += 1
        spiral[i][j] = 1
        if(dir == 0):
            if(j == size-1):
                dir = 1
                i += 1
            elif(j < (size - 2) and spiral[i][j+2] == 1):
                dir = 1
                i += 1
                if(spiral[i][j-1] or spiral[i+1][j]):
                    break
            else:
                j += 1
        elif(dir == 1):
            if(i == size-1):
                dir = 2
                j -= 1
            elif(i < (size - 2) and spiral[i+2][j] == 1):
                dir = 2
                j -= 1
                if(spiral[i][j-1] or spiral[i-1][j]):
                    break
            else:
                i += 1
        elif(dir == 2):
            if(j == 0):
                dir = 3
                i -= 1
            elif(j > 1 and spiral[i][j-2] == 1):
                dir = 3
                i -= 1
                if(spiral[i][j+1] or spiral[i-1][j]):
                    break
            else:
                j -= 1
        elif(dir == 3):
            if(i == 0):
                dir = 0
                j += 1
            elif(i > 1 and spiral[i-2][j] == 1):
                dir = 0
                j += 1
                if(spiral[i][j+1] == 1 or spiral[i+1][j]):
                    break
            else:
                i -= 1
    return spiral