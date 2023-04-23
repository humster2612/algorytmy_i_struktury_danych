numbers = [1, 2, 3, 11, 21, 111, 231]

def lexic_sort(numbers):
    sorted_numbers = []
    while len(numbers) > 0:
        smallest = min(numbers)
        sorted_numbers.append(smallest)
        numbers.remove(smallest)

    return sorted_numbers

print(lexic_sort(numbers))
