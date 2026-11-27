"""visual.py - графики конвейера."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def make_plots(df, out_dir='results'):
    os.makedirs(out_dir, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    counts = df['passed'].value_counts().sort_index()
    axes[0].bar(['не сдал', 'сдал'], counts.values)
    axes[0].set_title('Распределение целевой переменной')
    axes[0].set_ylabel('Количество студентов')
    cols = ['age', 'attendance', 'homework']
    corr = [df[c].corr(df['passed']) for c in cols]
    axes[1].bar(cols, corr)
    axes[1].axhline(0, color='gray', linewidth=0.8)
    axes[1].set_title('Связь признаков с результатом')
    axes[1].set_ylabel('Коэффициент корреляции')
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, 'pipeline_charts.png'))
    plt.close(fig)
