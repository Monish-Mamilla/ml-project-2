from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from src.data_loader import load_data
from src.preprocess import preprocess_data

def train_model():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    pipeline = Pipeline([
        ('preprocess', preprocess_data()),
        ('clf', LogisticRegression())
    ])
    pipeline.fit(X_train, y_train)
    return pipeline