import pandas as pd

players = {
    "name":   ["fufochka", "mr.night", "sally", "larry", "fren", "puhla"],
    "level":  [60, 45, 52, 78, 71, 33],
    "klass":  ["Воин", "Маг", "Шаман", "Лучник", "Демонолог", "Паладин"],
    "donate": [500, 1200, 300, 2400, 1800, 150]
}

df = pd.DataFrame(players)
print(df.head(6))

df.to_csv("dataset.csv", index=False, encoding="utf-8")

df2 = pd.read_csv("dataset.csv", encoding="utf-8")
df2.info()
result = df[(df["level"] > 40) & (df["klass"] == "Маг")]
print(result)
top = df.sort_values("donate", ascending=False)
print(top.head(3))
df["tax"] = df["donate"] * 0.13
print(df[["name", "donate", "tax"]].head(3))
avg = df.groupby("klass")["donate"].mean()
print(avg)
rich = df[df["level"] > 50]
rich.to_csv("rich_players.csv", index=False, encoding="utf-8")
print("Сохранено:", len(rich), "строк")
