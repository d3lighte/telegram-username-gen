from random import choice

def getRandomName(alphabet, lenght):
    s = ''
    items = list(alphabet)
    for _ in range(lenght):
        s += choice(items)
    return s