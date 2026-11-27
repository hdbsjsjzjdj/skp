"""main.py - полный конвейер обработки данных для ИИ."""
import os
from data_utils import generate_data, clean_data
from visual import make_plots
from model import (build_features, train_model,
                   save_model, load_model, FEATURES)
import pandas as pd
new_student = pd.DataFrame([[20, 90, 80, 0.8, 72.0]], columns=FEATURES)

def main():
    print('1. Загрузка данных...')
    df = generate_data()
    print(df.isnull().sum().to_dict())
    print(f'   Сырых строк: {len(df)}')
    print(f'   Дубликатов в сырых данных: {len(df) - len(df.drop_duplicates())}')
    after_dedup = len(df.drop_duplicates())
    print(after_dedup)
    df = clean_data(df)
    print(f'   Чистых строк: {len(df)}')

    print('2. Визуализация...')
    make_plots(df)
    print('   График: results/pipeline_charts.png')

    print('3. Признаки и обучение...')
    df = build_features(df)
    print(list(df.columns))
    from model import train_model_baseline
    print(f'   Контроль (3 признака): {train_model_baseline(df):.2f}')
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