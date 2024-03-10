# Importamos la clase LabelEncoder de la biblioteca scikit-learn
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

# Creamos una instancia de la clase LabelEncoder
encoder = LabelEncoder()

env = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # A
                    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], # B
                    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], # C
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # D
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], # E
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # F
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], # G
                    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1], # H
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], # I
                    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0], # J
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], # K
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]])# L

env2 = pd.DataFrame(env, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
                   index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])


# Creacion de los estados
# Diccionario de estados ( Estado - accion )
estados2 = {
    'A': 0 ,
    'B': 1 ,
    'C': 2 ,
    'D': 3 ,
    'E': 4 ,
    'F': 5 ,
    'G': 6 ,
    'H': 7 ,
    'I': 8 ,
    'J': 9 ,
    'K': 10 ,
    'L': 11 ,
}

# print(env)