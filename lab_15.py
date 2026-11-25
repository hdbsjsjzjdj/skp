#Задание №1
import os
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)   # папка для графиков

days = ["Пн", "Вт", "Ср", "Чт", "Пт"]
work = [2, 3.5, 7, 5, 9]               # условная сложность задач

plt.plot(days, work, "o-", color="steelblue", label="Сложность задач")
plt.xlabel("День недели")
plt.ylabel("Сложность")
plt.title("Сложность задач по дням")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("images/plot1.png", dpi=150)
plt.show()

#Задание №2
import os
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)   # папка для графиков

days = ["Пн", "Вт", "Ср", "Чт", "Пт"]
work = [2, 3.5, 7, 5, 9]               # условная сложность задач

plt.plot(days, work, "o-", color="steelblue", label="Сложность задач")
plt.xlabel("День недели")
plt.ylabel("Сложность")
plt.title("Сложность задач по дням")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("images/plot1.png", dpi=150)
plt.show()

#Задание №3
import os
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)

classes = ["Воин", "Маг", "Стрелок", "Паладин"]
counts  = [14, 9, 11, 6]

plt.bar(classes, counts, color=["#4C72B0", "#DD8452", "#55A868", "#C44E52"])
plt.xlabel("Класс персонажа")
plt.ylabel("Количество игроков")
plt.title("Распределение игроков по классам")
plt.savefig("images/bar_classes.png", dpi=150)
plt.show()

#Задание №4
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)

np.random.seed(7)
times = np.random.normal(loc=120, scale=25, size=500)  # время задач, мс

plt.hist(times, bins=30, color="steelblue", edgecolor="black")
plt.xlabel("Время выполнения, мс")
plt.ylabel("Количество задач")
plt.title("Распределение времени выполнения задач")
plt.savefig("images/hist_times.png", dpi=150)
plt.show()

print("Среднее:", times.mean().round(1))
print("Минимум:", times.min().round(1))
print("Максимум:", times.max().round(1))

#Задание №5
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)

np.random.seed(42)
x = np.arange(1, 21)                     # 20 точек
y = x * 3 + np.random.normal(0, 10, 20)  # линия + шум

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, y, "o-")
axes[0].set_title("Линейный график")
axes[0].set_xlabel("Время")
axes[0].set_ylabel("Значение")

axes[1].scatter(x, y, color="crimson")
axes[1].set_title("Точечная диаграмма")
axes[1].set_xlabel("Время")
axes[1].set_ylabel("Значение")

plt.tight_layout()
plt.savefig("images/subplots.png", dpi=150)
plt.show()

#Задание №7
import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)

df = pd.read_csv("dataset.csv")          # ваш датасет из лабы №14
counts = df["klass"].value_counts()

plt.bar(counts.index, counts.values, color="slateblue")
plt.title("Игроки по классам (из Pandas)")
plt.savefig("images/pandas_bar.png", dpi=150)
plt.show()

