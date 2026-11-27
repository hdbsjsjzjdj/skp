#Задание 1
"""data_utils.py - загрузка и очистка данных."""
import numpy as np
import pandas as pd

def generate_data(n=200, seed=42):
    """Создаёт сырой датасет студентов с грязью."""
    rng = np.random.default_rng(seed)
    ages = rng.integers(17, 40, n)
    attendance = np.round(rng.uniform(30, 100, n), 1)
    homework = np.round(rng.uniform(0, 100, n), 1)
    logit = -6 + 0.09 * attendance + 0.03 * homework - 0.02 * ages
    prob = 1 / (1 + np.exp(-logit))
    passed = (rng.uniform(0, 1, n) < prob).astype(int)
    df = pd.DataFrame({'age': ages,
                       'attendance': attendance,
                       'homework': homework,
                       'passed': passed})
    dup = df.sample(6, random_state=seed + 1)   # дубликаты
    df = pd.concat([df, dup], ignore_index=True)
    for col in ['age', 'attendance', 'homework']:  # пропуски
        idx = rng.choice(len(df), 4, replace=False)
        df.loc[idx, col] = np.nan
    return df

def clean_data(df):
    """Очистка: дубликаты и пропуски медианой."""
    df = df.drop_duplicates().copy()
    df = df.dropna(subset=['passed']).copy()
    for col in ['age', 'attendance', 'homework']:  # число, а не строка
        df[col] = df[col].fillna(df[col].median())
    return df

from data_utils import generate_data, clean_data
raw = generate_data()
print(len(raw), len(raw.drop_duplicates()))

#Задание 2
"""visual.py - графики конвейера."""
import os
import matplotlib
matplotlib.use('Agg')   # без окна: только сохранение в файл
import matplotlib.pyplot as plt

def make_plots(df, out_dir='results'):
    os.makedirs(out_dir, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # График 1: распределение целевой переменной
    counts = df['passed'].value_counts().sort_index()
    axes[0].bar(['не сдал', 'сдал'], counts.values)
    axes[0].set_title('Распределение целевой переменной')
    axes[0].set_ylabel('Количество студентов')

    # График 2: корреляция признаков с целевой переменной
    cols = ['age', 'attendance', 'homework']
    corr = [df[c].corr(df['passed']) for c in cols]
    axes[1].bar(cols, corr)
    axes[1].axhline(0, color='gray', linewidth=0.8)
    axes[1].set_title('Связь признаков с результатом')
    axes[1].set_ylabel('Коэффициент корреляции')

    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, 'pipeline_charts.png'))
    plt.close(fig)

import os
print(os.path.exists('results/pipeline_charts.png'))

#Задание 3
"""model.py - признаки, обучение и сохранение модели."""
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def build_features(df):
    """Feature Engineering: два новых признака."""
    df = df.copy()
    df['homework_rate'] = df['homework'] / 100
    df['att_x_hw'] = df['attendance'] * df['homework_rate']
    return df

FEATURES = ['age', 'attendance', 'homework',
            'homework_rate', 'att_x_hw']
TARGET = 'passed'

def train_model(df):
    X = df[FEATURES]
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    return model, acc, X_test, y_test

def save_model(model, path='results/model.pkl'):
    with open(path, 'wb') as f:      # wb = write binary
        pickle.dump(model, f)

def load_model(path='results/model.pkl'):
    with open(path, 'rb') as f:      # rb = read binary
        return pickle.load(f)

#Заданеи 4
"""main.py - полный конвейер обработки данных для ИИ."""
import os
from data_utils import generate_data, clean_data
from visual import make_plots
from model import (build_features, train_model,
                   save_model, load_model, FEATURES)

def main():
    print('1. Загрузка данных...')
    df = generate_data()
    print(f'   Сырых строк: {len(df)}')
    df = clean_data(df)
    print(f'   Чистых строк: {len(df)}')

    print('2. Визуализация...')
    make_plots(df)
    print('   График: results/pipeline_charts.png')

    print('3. Признаки и обучение...')
    df = build_features(df)
    model, acc, X_test, y_test = train_model(df)
    print(f'   Accuracy: {acc:.2f}')
    for name, c in zip(FEATURES, model.coef_[0]):
        print(f'   {name:>14}: {c:+.3f}')

    print('4. Сохранение модели...')
    os.makedirs('results', exist_ok=True)
    save_model(model)
    model2 = load_model()
    new_student = [[20, 90, 80, 0.8, 72.0]]
    p = model2.predict_proba(new_student)[0][1]
    print(f'   Новый студент: сдал={model2.predict(new_student)[0]},'
          f' вероятность={p:.2f}')
    print('Конвейер завершён.')

if __name__ == '__main__':
    main()
