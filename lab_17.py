#Задание №1
import pandas as pd
 
# Грязные данные: пропуски (None), дубликаты, текст вместо чисел
data = {
    "name": ["Анна", "Борис", "Виктор", "Анна", "Дмитрий",
             "Елена", "Борис", "Жанна", "Захар", "Ирина"],
    "age": [25, 34, None, 25, 45, 29, 34, None, 150, 31],
    "city": ["Москва", None, "Казань", "Москва", "Сочи",
             "Москва", "Казань", "Тверь", "Омск", "Уфа"],
    "salary": [50000, 60000, 55000, 50000, 70000,
               None, 60000, 52000, 90000, 58000],
    "experience": ["3", "5", "2", "3", "10",
                   "7", "5", None, "20", "4"],
}
df = pd.DataFrame(data)
print("=== Задание 1: грязный датасет ===")
print(df)
#Задание №2
print("=== Задание 2: сколько пропусков в каждом столбце ===")
print(df.isnull().sum())
#Задание №3
print("=== Задание 3: удаляем строки с пропуском имени или возраста ===")
df = df.dropna(subset=["name", "age"])
print(f"Осталось строк: {len(df)}")
print(df)

#Задание №4
print("=== Задание 4: заполняем пропуски зарплаты средним ===")
mean_salary = df["salary"].mean()
print(f"Средняя зарплата: {mean_salary}")
df["salary"] = df["salary"].fillna(mean_salary)
print(df)

#Задание №5
print("=== Задание 5: удаляем дубликаты ===")
print(f"Дубликатов найдено: {df.duplicated().sum()}")
df = df.drop_duplicates()
print(f"Осталось строк: {len(df)}")
print(df)

#Задание №6
print("=== Задание 6: выбросы — возраст больше 100 ===")
mask = df["age"] > 100
print("Выбросы:")
print(df[mask])
median_age = df.loc[~mask, "age"].median()
print(f"Медиана без выбросов: {median_age}")
df.loc[mask, "age"] = median_age
print(df)

#Задание №7
print("=== Задание 7: приводим столбец experience к числу ===")
df["experience"] = pd.to_numeric(df["experience"], errors="coerce")
df["experience"] = df["experience"].fillna(df["experience"].mean())
df["experience"] = df["experience"].astype(int)
print(df.dtypes)
print(df)

#Задание №8
print("=== Задание 8: сохраняем очищенные данные ===")
df.to_csv("clean_data.csv", index=False)
print("Файл clean_data.csv сохранён.")
print(df.info())
