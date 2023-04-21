numbers = [-3,5, 8, 3, 1, 9, 2,-2]
min_value = numbers[0]
i = 0
while i < len(numbers):
    if numbers[i] < min_value:
        min_value = numbers[i]
    i+=1
print(f"Minimalna wartość w tablicy to: {min_value}")
