def calculate_segments(n, arr):
    target_value = 1
    index = 0
    count = 0

    while index < n:
        if arr[index] == target_value:
            count += 1
            target_value += 1
            while index < n and arr[index] != target_value:
                index += 1
        index += 1
    return count if target_value > 1 else 0

n = int(input("Введите длину массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
print(calculate_segments(n, arr))
