def pow(a, b):
    if b < 0:
        a = 1 / a
        b *= -1
    if b == 0:
        return 1
    return a * pow(a, b - 1)
