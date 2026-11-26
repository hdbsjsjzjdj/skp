#Задание 1
import numpy as np
from sklearn.model_selection import train_test_split
 
np.random.seed(42)                      # чтобы результат был одинаковым
hours = np.random.uniform(0, 12, 30)    # 30 студентов, от 0 до 12 часов
grade = 40 + 5 * hours + np.random.normal(0, 5, 30)
 
X = hours.reshape(-1, 1)                # X — таблица: 30 строк, 1 столбец
y = grade                               # y — один столбец ответов
 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print("Обучающая выборка:", X_train.shape)
print("Тестовая выборка:", X_test.shape)

#Задание 2
from sklearn.linear_model import LinearRegression
 
model = LinearRegression()
model.fit(X_train, y_train)
 
print("Наклон (k):", round(model.coef_[0], 2))
print("Свободный член (b):", round(model.intercept_, 2))

#Задание 3
y_pred = model.predict(X_test)
print("Предсказания:", np.round(y_pred[:3], 1))
print("Реальные:     ", np.round(y_test[:3], 1))
 
new_hours = np.array([[6.0]])           # новый студент: 6 часов
print("За 6 часов модель обещает:", round(model.predict(new_hours)[0], 1))

#Задание  4
from sklearn.metrics import mean_absolute_error
 
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", round(mae, 2))
print("Модель ошибается в среднем на", round(mae, 1), "балла")

#Задание 5
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
 
np.random.seed(42)
n = 30
age = np.random.randint(14, 60, n)
minutes = np.random.randint(10, 400, n)
buy = ((age < 35) & (minutes > 120)).astype(int)
flip = np.random.choice(n, 3, replace=False)
buy[flip] = 1 - buy[flip]               # шум: 3 «исключения из правила»
 
df = pd.DataFrame({"age": age, "minutes": minutes, "bought": buy})
print("Баланс классов:", df["bought"].value_counts().to_dict())
 
Xk = df[["age", "minutes"]]             # два признака
yk = df["bought"]                       # метка
Xk_train, Xk_test, yk_train, yk_test = train_test_split(
    Xk, yk, test_size=0.3, random_state=42, stratify=yk
)
 
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(Xk_train, yk_train)
pred = knn.predict(Xk_test)
print("Accuracy kNN:", round(accuracy_score(yk_test, pred), 2))
 
new_user = pd.DataFrame({"age": [25], "minutes": [300]})
print("Новый пользователь 25 лет, 300 минут -> купит?",
      knn.predict(new_user)[0])

#Задание 6
import matplotlib.pyplot as plt
import os
 
os.makedirs("images", exist_ok=True)
 
plt.figure(figsize=(7, 4))
plt.scatter(X_train[:, 0], y_train, label="Обучающие данные")
plt.scatter(X_test[:, 0], y_test, color="red", label="Тестовые данные")
xs = np.linspace(0, 12, 100)
plt.plot(xs, model.intercept_ + model.coef_[0] * xs,
         "g-", label="Линия регрессии")
plt.xlabel("Часы подготовки")
plt.ylabel("Оценка")
plt.title("Линейная регрессия: часы -> оценка")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("images/regression.png", dpi=150, bbox_inches="tight")
print("График сохранён в images/regression.png")
