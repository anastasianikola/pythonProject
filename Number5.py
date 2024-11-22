def can_satisfy_conditions(n, m, queries):
    # Изначальный массив значений
    a = [0] * n

    for l, r, cond, x in queries:
        # Преобразуем индексы в 0-базисные
        l -= 1
        r -= 1

        # Рассчитываем текущую сумму для диапазона [L, R]
        current_sum = sum(a[l:r + 1])

        # Обновляем массив, чтобы удовлетворить запрос
        if cond == ">=":
            if current_sum < x:
                # Требуется увеличить текущую сумму
                diff = x - current_sum
                for i in range(l, r + 1):
                    a[i] += diff // (r - l + 1)
        elif cond == "<=":
            if current_sum > x:
                # Требуется уменьшить текущую сумму
                diff = current_sum - x
                for i in range(l, r + 1):
                    a[i] -= diff // (r - l + 1)

    # Проверяем все запросы заново
    for l, r, cond, x in queries:
        l -= 1
        r -= 1
        current_sum = sum(a[l:r + 1])
        if cond == ">=" and current_sum < x:
            return "NO"
        elif cond == "<=" and current_sum > x:
            return "NO"

    return "YES"


# Ввод данных
n, m = map(int, input().split())
queries = []

for _ in range(m):
    line = input().strip()
    if line:  # Проверяем, что строка не пуста
        parts = line.split()
        if len(parts) == 4:  # Убедимся, что есть все четыре элемента
            l, r = map(int, parts[:2])
            cond = parts[2]
            x = int(parts[3])
            queries.append((l, r, cond, x))
        else:
            print("Некорректный ввод строки:", line)
            exit(1)

# Решение задачи
result = can_satisfy_conditions(n, m, queries)

# Вывод результата
print(result)
