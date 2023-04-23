def dec2bin(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = dec2bin(num // 2)
        result = result * 10 + num % 2
        print(result)
        return result
dec2bin(103)
