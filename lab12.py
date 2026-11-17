#Задание 1
print("--- Задание 1 ---")
try:
    a = int(input("Введи первое число: "))
    b = int(input("Введи второе число: "))
    print("Результат:", a / b)
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")


#Задание 2
print("\n--- Задание 2 ---")
try:
    x = int(input("Введи число: "))
    print("Результат:", 10 / x)
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
finally:
    print("Программа завершена")


#Задание 3
print("\n--- Задание 3 ---")
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет\n")
    f.write("Как дела?\n")
    f.write("Пока\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

print(lines)
real_lines = [x for x in lines if x != ""]
print("Строк в файле:", len(real_lines))


#Задание 4
print("\n--- Задание 4 ---")
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("Ещё одна строка\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())


#Задание 5
class Streamer:
    def __init__(self, nickname, subscribers, donates):
        self.nickname = nickname
        self.subscribers = subscribers
        self.donates = donates

    def to_line(self):
        donates_str = ",".join(str(d) for d in self.donates)
        return f"{self.nickname};{self.subscribers};{donates_str}"


def streamer_from_line(line):
    nickname, subscribers, donates_str = line.strip().split(";")
    donates = [] if donates_str == "" else [int(d) for d in donates_str.split(",")]
    return Streamer(nickname, int(subscribers), donates)


#Задание 6
def save_to_file(objects, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(obj.to_line() + "\n")


def load_from_file(filename):
    objects = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                objects.append(streamer_from_line(line))
    except FileNotFoundError:
        print("Файл не найден, начинаем с пустого списка.")
    except ValueError:
        print("Ошибка в формате данных.")
    return objects


#Задание 7
print("\n--- Задание 7 ---")
def print_streamer(s):
    avg = sum(s.donates) / len(s.donates) if s.donates else 0
    print(f"Стример: {s.nickname}")
    print(f"Подписчики: {s.subscribers}")
    print(f"Всего донатов: {sum(s.donates)}")
    print(f"Средний донат: {avg}")

streamers = [
    Streamer("GolubKin", 1200, [300, 350]),
    Streamer("FrostMiron", 800, [100, 200, 150]),
    Streamer("Nova", 2500, [500]),
]

save_to_file(streamers, "data.txt")

streamers = []
streamers = load_from_file("data.txt")

for s in streamers:
    print_streamer(s)
    #Задание 8
print("\n--- Задание 8 ---")
class Player:
    def __init__(self, name, points=0, level=1):
        self.name = name
        self.points = points
        self.level = level

    def to_line(self):
        return f"{self.name};{self.points};{self.level}"

def player_from_line(line):
    name, points, level = line.strip().split(";")
    return Player(name, int(points), int(level))

def save_player(player, filename="player.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(player.to_line())

def load_player(filename="player.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return player_from_line(f.read())
    except FileNotFoundError:
        return Player(input("Введи имя игрока: "))

# Раскомментируй код ниже, если хочешь запустить игру при проверке
# player = load_player()
# print(f"С возвращением, {player.name}! Очки: {player.points}")
# while True:
#     answer = input("Играем ещё раунд? (да/нет): ")
#     if answer == "нет":
#         print("Пока!")
#         break
#     player.points += 10
#     player.level = player.points // 50 + 1
#     save_player(player)
#     print(f"Очки сохранены: {player.points}, уровень: {player.level}")


#Задание 9
print("\n--- Задание 9 ---")
def task9():
    filename = input("Введи имя файла для чтения: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except PermissionError:
        print("Ошибка: Нет прав на чтение файла.")
    except UnicodeDecodeError:
        print("Ошибка: Неверная кодировка файла (не UTF-8).")

# task9() # Раскомментируй для проверки


#Задание 10
print("\n--- Задание 10 ---")
# Формат: поля разделены "|", донаты — через запятую.
def save_custom(objects, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(obj.to_line().replace(";", "|") + "\n")

def load_custom(filename):
    objects = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                objects.append(streamer_from_line(line.replace("|", ";")))
    except FileNotFoundError:
        print("Файл не найден.")
    except ValueError:
        print("Ошибка формата данных.")
    return objects

# Тестируем свой формат
save_custom(streamers, "custom_data.txt")
loaded_custom = load_custom("custom_data.txt")
print(f"Загружено из своего формата: {len(loaded_custom)} объектов")