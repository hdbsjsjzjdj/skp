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
    dup = df.sample(6, random_state=seed + 1)
    df = pd.concat([df, dup], ignore_index=True)
    for col in ['age', 'attendance', 'homework']:
        idx = rng.choice(len(df), 4, replace=False)
        df.loc[idx, col] = np.nan
    return df

def clean_data(df):
    """Очистка: дубликаты и пропуски медианой."""
    df = df.drop_duplicates().copy()
    df = df.dropna(subset=['passed']).copy()
    for col in ['age', 'attendance', 'homework']:
        df[col] = df[col].fillna(df[col].median())
    return df
