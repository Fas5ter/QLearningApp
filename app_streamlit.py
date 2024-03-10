import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from modelo import env2, env, estados2

from QLearning import ObtenerQ

# Configuramos la pagina de Streamlit
st.set_page_config(page_title="App de Q-Learning",
                #    page_icon=":robot:", layout="wide")
                page_icon="coco.ico", 
                layout="centered",
                initial_sidebar_state="auto")

# Definimos el titulo y descripción de la app

st.title("App que calcula la mejor ruta usando el algoritmo de Q-Learning")
st.markdown("""Esta aplicacion web utiliza el algoritmo de Q-Learning para calcular la mejor ruta desde un punto de inicio a un punto final, tomando un punto medio para pasar por ahi de preferencia.""")
st.markdown("""El algoritmo de Q-Learning es un algoritmo de aprendizaje por refuerzo que busca encontrar la mejor ruta para llegar a un destino, tomando en cuenta la experiencia previa y el refuerzo positivo o negativo que se le da al agente.""")
st.markdown("""---""")

# Mostrar el entorno de la aplicacion
st.markdown("""Entorno de la aplicacion:""")
st.write(env2)

# st.write(estados2.keys())
st.markdown("""---""")


# Cargamos y mostramos el logo en la barra lateral
logo = "coco.jpeg"
st.sidebar.image(logo, width=150, use_column_width=True)
# Añadimos un encabezado para la seccion de datos del usuario en la barra lateral
st.sidebar.markdown("""---""")
st.sidebar.header("Datos ingresados por el usuario")
# Ingresamos el punto de inicio
inicio = st.sidebar.text_input("Punto de inicio", "E")
# Ingresamos el punto medio
medio = st.sidebar.text_input("Punto medio", "F")
# Ingresamos el punto final
final = st.sidebar.text_input("Punto final", "G")
ruta, Q = ObtenerQ(env, estados2,inicio, final, medio)
st.sidebar.markdown("""---""")
# Permitimos al usuario ingresar los datos de la ruta
st.sidebar.subheader("Datos de la ruta")
st.sidebar.markdown("""---""")

# Mostrar la matriz de Q
st.markdown("""Matriz de rutas aplicando Q-Learning:""")
st.write(Q.astype(int))
st.markdown("""---""")
# Mostrar la ruta mas corta
st.markdown(f"La ruta mas corta es: {ruta}")