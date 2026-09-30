import os
import pandas as pd
import random
from variables_categoricas import *


#TODO: Limpia la terminal
def Cls():
    os.system('cls' if os.name == 'nt' else 'clear')

Cls()

#TODO: variables:
# print(frecuencia_uso)
# print(red_social_principal)
# print(tipo_contenido)
# print(publica_contenido)
# print(uso_nocturno)
# print(notificaciones)
# print(motivo_principal)
# print(nivel_satisfaccion)

#? edad = [13, 65]
#? horas_diarias = [0.5, 12]
#? sesiones_diarias = [1, 30]
#? interaccion_diaria = [0, 200]

#TODO: Funciones:
def generar_null(valor, probabilidad=0.10):
    if random.random() < probabilidad:
        return None
    return valor

#TODO: Generar dataset:
datos = []

for i in range(100):

    registro = {
        "edad": generar_null(random.randint(13, 65)),

        "red_social_principal": generar_null(
            random.choice(red_social_principal)
        ),

        "frecuencia_uso": generar_null(
            random.choice(frecuencia_uso)
        ),

        "horas_diarias": generar_null(
            round(random.uniform(0.5, 12), 1)
        ),

        "sesiones_diarias": generar_null(
            random.randint(1, 30)
        ),

        "tipo_contenido": generar_null(
            random.choice(tipo_contenido)
        ),

        "interaccion_diaria": generar_null(
            random.randint(0, 200)
        ),

        "publica_contenido": generar_null(
            random.choice(publica_contenido)
        ),

        "uso_nocturno": generar_null(
            random.choice(uso_nocturno)
        ),

        "notificaciones": generar_null(
            random.choice(notificaciones)
        ),

        "motivo_principal": generar_null(
            random.choice(motivo_principal)
        ),

        "nivel_satisfaccion": generar_null(
            random.choice(nivel_satisfaccion)
        )
    }

    datos.append(registro)


#TODO: Crear DataFrame:
df = pd.DataFrame(datos)

#TODO: Guardar el DataFrame como CSV:
df.to_csv(
    "redes_sociales.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Dataset creado correctamente.")
print(f"Registros: {len(df)}")
print(f"Columnas: {len(df.columns)}")