from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np2

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        try:
          return data.drop(labels=self.columns, axis='columns')
        except AttributeError as error:
          return data
