import requests
import pandas as pd
import json
import os
from datetime import datetime
import urllib3

# Отключаем предупреждение о небезопасном запросе (нужно из-за verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://jsonplaceholder.typicode.com/users"

#ЗАДАНИЕ 1
try:
    # Добавлен verify=False для обхода ошибок SSL на Windows
    response = requests.get(url, verify=False, timeout=10)
    print("Статус-код:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Ошибка сети:", e)
    response = None

#ЗАДАНИЕ 2
if response and response.status_code == 200:
    data = response.json()
    print("\nВсего пользователей:", len(data))
    
    print("\nСписок пользователей (Имя - Email):")
    for user in data:
        
        print(user.get("name", "Нет имени"), "-", user.get("email", "Нет email"))
        
    # 
    if data and "address" in data[0]:
        print("\nГород первого пользователя:", data[0]["address"]["city"])

    #ЗАДАНИЕ 3
    df = pd.DataFrame(data)
    print("\n--- Полная таблица (первые 5 строк) ---")
    print(df.head())
    
    flat_columns = ["id", "name", "username", "email", "phone", "website"]
    df = df[flat_columns]
    print("\n--- Таблица после удаления вложенных словарей ---")
    print(df.head())

    #ЗАДАНИЕ 4
    os.makedirs("data", exist_ok=True)
    
    df.to_csv("data/users.csv", index=False, encoding="utf-8")
    
    with open("data/users.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("\nФайлы сохранены в папку data/:")
    print(os.listdir("data"))

    #ЗАДАНИЕ 5
    dirty = [dict(u) for u in data]
    dirty[0]["email"] = None  
    dirty.append(dirty[1])   
    
    df_dirty = pd.DataFrame(dirty)
    df_dirty = df_dirty[["id", "name", "email"]]
    
    print("\n--- Анализ 'грязных' данных ---")
    print("Пропуски по колонкам:")
    print(df_dirty.isnull().sum())
    print("Найдено дубликатов:", df_dirty.duplicated().sum())

    #ЗАДАНИЕ 6
    def fetch_and_backup(api_url, folder="data"):
        """Делает GET-запрос и сохраняет ответ с датой в имени файла."""
        try:
            resp = requests.get(api_url, verify=False, timeout=10)
            if resp.status_code != 200:
                print("Запрос не удался, код:", resp.status_code)
                return None
            
            api_data = resp.json()
            stamp = datetime.now().strftime("%Y-%m-%d")
            os.makedirs(folder, exist_ok=True)
            
           
            path = os.path.join(folder, f"users_{stamp}.json")
            
            with open(path, "w", encoding="utf-8") as f:
                json.dump(api_data, f, ensure_ascii=False, indent=2)
            
            print(f"\nБэкап сохранён: {path}")
            return pd.DataFrame(api_data)
        except Exception as e:
            print("Ошибка в функции бэкапа:", e)
            return None

   
    df_backup = fetch_and_backup(url)

else:
    print("\n--- ИМИТАЦИЯ API (Задание 5) ---")
    print("Сетевой запрос не удался. Пробуем прочитать локальный файл.")
    
    try:
        with open("data/users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        print(df.head())
    except FileNotFoundError:
        print("Файл data/users.json не найден. Сначала нужно выполнить задание 4 при наличии интернета.")