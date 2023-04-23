def max_element(vec):
    n = len(vec)
    if n == 1:
        return vec[0]
    elif n == 2:
        if vec[0] > vec[1]:
            return vec[0]
        else:
            return vec[1]
    else:
        mid = n // 2    
        max1 = max_element(vec[:mid])
        max2 = max_element(vec[mid:])
        if max1 > max2:
            return max1
        else:
            return max2
vec = [2,4,5]
max_num = max_element(vec)
print(max_num)
