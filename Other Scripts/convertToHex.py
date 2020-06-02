def hex2(color):
    return (hex(color).split('x')[-1] if color > 15 else "0" + hex(color).split('x')[-1]).upper()

def rgb(r, g, b):
    r = 255 if r > 255 else r
    r = 0 if r < 0 else r
    g = 255 if g > 255 else g
    g = 0 if g < 0 else g
    b = 255 if b > 255 else b
    b = 0 if b < 0 else b
    return hex2(r) + hex2(g) + hex2(b)