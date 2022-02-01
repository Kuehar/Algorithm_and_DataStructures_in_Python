def recursvie(num):
    if num <= 0:
        return 1
    return num*recursvie(num-1)