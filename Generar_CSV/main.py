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


#TODO: Generar dataset:
datos = []

for i in range(100):

    registro = {
        "edad": random.randint(13, 65),

        "red_social_principal": random.choice(
            red_social_principal
        ),

        "frecuencia_uso": random.choice(
            frecuencia_uso
        ),

        "horas_diarias": round(
            random.uniform(0.5, 12), 1
        ),

        "sesiones_diarias": random.randint(
            1, 30
        ),

        "tipo_contenido": random.choice(
            tipo_contenido
        ),

        "interaccion_diaria": random.randint(
            0, 200
        ),

        "publica_contenido": random.choice(
            publica_contenido
        ),

        "uso_nocturno": random.choice(
            uso_nocturno
        ),

        "notificaciones": random.choice(
            notificaciones
        ),

        "motivo_principal": random.choice(
            motivo_principal
        ),

        "nivel_satisfaccion": random.choice(
            nivel_satisfaccion
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