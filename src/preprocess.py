from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

def preprocess_data():
    numeric_features = ['feature1', 'feature2']
    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    return ColumnTransformer([
        ('num', numeric_transformer, numeric_features),
    ])