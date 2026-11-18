"""
Лабораторная работа № 13.
Тема: «Библиотека NumPy: массивы, векторные операции и статистика».
"""

import numpy as np

# --- ЗАДАНИЕ 1. Первый массив ---
print("\n--- Задание 1 ---")
numbers = [3, 7, 1, 9, 4]
arr = np.array(numbers)
print("Тип:", type(arr))
print("Форма:", arr.shape)
print("Размер:", arr.size)
print("Массив:", arr)

# --- ЗАДАНИЕ 2. Векторная операция ---
print("\n--- Задание 2 ---")
celsius = np.array([0, 10, 20, 30, 40])
fahrenheit = celsius * 9 / 5 + 32
print("Цельсии:   ", celsius)
print("Фаренгейты:", fahrenheit)

# --- ЗАДАНИЕ 3. Статистика ---
print("\n--- Задание 3 ---")
times = np.array([120, 95, 88, 102, 77, 110, 85])
print("Среднее время:     ", np.mean(times))
print("Максимум:          ", np.max(times))
print("Минимум:           ", np.min(times))
print("Станд. отклонение: ", np.std(times))
print("Сумма:             ", np.sum(times))

# --- ЗАДАНИЕ 4. Матрица весов ---
print("\n--- Задание 4 ---")
weights = np.array([[0.1, 0.2, 0.3],
                    [0.4, 0.5, 0.6],
                    [0.7, 0.8, 0.9]])
print("Матрица:\n", weights)
print("Форма:", weights.shape)
print("Первая строка:    ", weights[0, :])
print("Последний столбец:", weights[:, -1])
print("Элемент [1][2]:   ", weights[1, 2])

#ЗАДАНИЕ 5. Маска ---
print("\n--- Задание 5 ---")
randoms = np.random.randint(1, 101, size=100)
mask = randoms > 50
big = randoms[mask]
print("Всего чисел:      ", randoms.size)
print("Чисел больше 50:  ", big.size)
print("Отобранные числа: ", big)

#ЗАДАНИЕ 6
print("\n--- Задание 6 ---")
grades = np.array([[5, 4, 3],
                   [4, 4, 5],
                   [3, 5, 5],
                   [4, 3, 4],
                   [5, 5, 4]])
by_student = grades.mean(axis=1)
by_subject = grades.mean(axis=0)
print("Средний балл каждого студента:", by_student)
print("Средний балл по предметам:     ", by_subject)