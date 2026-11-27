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
    with open(path, 'wb') as f:
        pickle.dump(model, f)

def load_model(path='results/model.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)


# Контрольный эксперимент: модель без новых признаков.
BASE_FEATURES = ['age', 'attendance', 'homework']

def train_model_baseline(df):
    X = df[BASE_FEATURES]
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return accuracy_score(y_test, model.predict(X_test))
