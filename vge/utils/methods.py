def clamp(num, min_, max_):
    if num < min_:
        num = min_
    elif num > max_:
        num = max_
    
    return num
