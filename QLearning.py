import streamlit as st
import numpy as np

gamma = 0.75 # Descuento
alpha = 0.9 # Aprendizaje

def Ambiente(num_estados: int, env):
    estado_actual = np.random.randint(0,num_estados)
    accion_realizable = []
    for j in range(num_estados):
        if env[estado_actual, j] > 0:
            accion_realizable.append(j)
    estado_siguiente = np.random.choice(accion_realizable)
    return[estado_actual, estado_siguiente]

def Qlearning(estado_actual: int, estado_siguiente : int, gamma: float, alpha: float, env, Q):
    TD = env[estado_actual, estado_siguiente] + gamma*Q[estado_siguiente, np.argmax(Q[estado_siguiente,])]- Q[estado_actual, estado_siguiente]
    Q[estado_actual, estado_siguiente] = Q[estado_actual, estado_siguiente] + alpha*TD
    return Q

def Obtener_clave_por_valor(diccionario, valor):
    for clave, val in diccionario.items():
        if val == valor:
            return clave
    return None  # Si el valor no se encuentra en el diccionario

def Ruta(indice1, indice3, inicio, medio, fin, estados, Q):
    ruta = [inicio]

    # Añadir el primer paso de la ruta
    # Q = Q.astype(int)
    x = Q[indice1].argmax()

    # Añadir los demas pasos de la ruta
    while True:
        if Obtener_clave_por_valor(estados, x) == fin:
            ruta.append(Obtener_clave_por_valor(estados, x))
            break
        else:
            ruta.append(Obtener_clave_por_valor(estados, x))
            if Obtener_clave_por_valor(estados, x) == medio:
                Q[indice3,indice3] = 0
            indice1 = estados.get(Obtener_clave_por_valor(estados, x))
            x = Q[indice1].argmax()
    return ruta

def ObtenerQ(env, estados2, inicio, fin, medio):
    lenght = len(env)
    # Indice del inicio
    indice1 = estados2.get(inicio)

    # Indice del final
    indice2 = estados2.get(fin)
    env[indice2,indice2] = 1000

    # Indice valor intermedio
    indice3 = estados2.get(medio)
    env[indice3,indice3] = 500

    # Q-Learning
    Q = np.array(np.zeros([lenght,lenght]))
    for i in range(1000):
        estados = Ambiente(lenght, env)
        Q = Qlearning(estados[0], estados[1], gamma, alpha, env, Q)


    ruta_final = Ruta(indice1, indice3, inicio, medio, fin, estados2, Q)
    valor_medio = Q[indice3,indice3]
    Q[indice3,indice3] = valor_medio

    # Reseteamos el env
    env[indice2,indice2] = 0
    env[indice3,indice3] = 0

    return ruta_final, Q

if __name__ == "__main__":

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

    inicio = str(input("Ingresa desde donde quieres comenzar (La letra): ")).upper()
    fin = str(input("Ingresa a donde quieres ir (La letra): ")).upper()
    medio = str(input("Ingresa por donde quieres que pase preferentemente (La letra): ")).upper()
    ruta, Q = ObtenerQ(env, estados2,inicio, fin, medio)
    print(f"La ruta mas corta es: {ruta}")
    print(Q.astype(int))
    while True:
        opt = str(input("Ingresa la opción que deseas realizar\n\
        1.) Cambiar el punto de inicio.\n\
        2.) Cambiar el punto medio.\n\
        3.) Cambiar el punto final.\n\
        4.) Cambiar todos los puntos.\n\
        5.) Salir.\n\
        Opcion = "))
        match opt:
            case "1":
                inicio = str(input("Ingresa desde donde quieres comenzar (La letra): ")).upper()
                indice1 = estados2.get(inicio)
                indice3 = estados2.get(medio)
                rutaN = Ruta(indice1, indice3, inicio, medio, fin, estados2, Q)
                print(f"La ruta mas corta es: {rutaN}")
                print(Q.astype(int))
            case "2":
                medio = str(input("Ingresa por donde quieres que pase preferentemente (La letra): ")).upper()
                rutaN, Q = ObtenerQ(env, estados2, inicio, fin, medio)
                print(f"La ruta mas corta es: {rutaN}")
                print(Q.astype(int))
            case "3":
                fin = str(input("Ingresa a donde quieres ir (La letra): ")).upper()
                rutaN, Q = ObtenerQ(env, estados2, inicio, fin, medio)
                print(f"La ruta mas corta es: {rutaN}")
                print(Q.astype(int))
            case "4":
                inicio = str(input("Ingresa desde donde quieres comenzar (La letra): ")).upper()
                fin = str(input("Ingresa a donde quieres ir (La letra): ")).upper()
                medio = str(input("Ingresa por donde quieres que pase preferentemente (La letra): ")).upper()
                rutaN, Q= ObtenerQ(env, estados2, inicio, fin, medio)
                print(f"La ruta mas corta es: {rutaN}")
                print(Q.astype(int))
            case "5":
                print("Saliendo...")
                break
            case default:
                print("Opcion incorrecta, no existe esa opción")