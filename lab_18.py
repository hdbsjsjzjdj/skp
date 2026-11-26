#Задание 1
import pandas as pd
 
data = {
    "text": [
        "Отличный сервис, всё работает быстро и без сбоев",
        "Ужасное приложение, постоянно зависает и вылетает",
        "Поддержка ответила быстро, проблему решили за час",
        "Не рекомендую, потратил деньги зря",
        "Функционал удобный, интерфейс приятный, всё нравится",
        "Дизайн хороший, но тормозит на старом телефоне",
        "Полное разочарование, ничего не работает как надо",
        "Лучшее обновление за год, спасибо разработчикам",
        "Всё супер, приложение стало заметно быстрее",
        "Служба поддержки на высоте, отвечает за пять минут",
    ]
}
df = pd.DataFrame(data)
print(df)

#Заднание 2
labels = [1, 0, 1, 0, 1, 1, 0, 1, 1, 1]  # 1 — позитив, 0 — негатив
df["label"] = labels
print(df[["text", "label"]])

#Задание 3
df["text_length"] = df["text"].str.len()
print(df[["text", "text_length"]])

#Задание 4
df["word_count"] = df["text"].str.split().str.len()
print(df[["text", "text_length", "word_count"]])

#Задание 5
balance = df["label"].value_counts()
print(balance)
 
total = len(df)
print(f"Позитивных: {int((df['label'] == 1).sum())} из {total} "
      f"({(df['label'] == 1).mean() * 100:.1f}%)")
print(f"Негативных: {int((df['label'] == 0).sum())} из {total} "
      f"({(df['label'] == 0).mean() * 100:.1f}%)")

#Задание 6
final = df[["text_length", "word_count", "label"]].copy()
final.to_csv("labeled_dataset.csv", index=False, encoding="utf-8-sig")
print(final.head(10))

#Задание 7
df["has_exclamation"] = df["text"].str.contains("!").astype(int)
print(df[["text", "has_exclamation"]])
#Задание
import matplotlib.pyplot as plt
import os
os.makedirs("images", exist_ok=True)
 
balance.plot(kind="bar")
plt.title("Баланс классов")
plt.xlabel("Метка")
plt.ylabel("Количество отзывов")
plt.tight_layout()
plt.savefig("images/classes.png", dpi=150)
plt.show()
