import os
import pandas as pd
import random
from variables_categoricas import *
from funciones import *


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

#? edad = [13, 54]
#? horas_diarias = [0.5, 12]
#? sesiones_diarias = [1, 30]
#? interaccion_diaria = [0, 200]


#TODO: Generar dataset:
datos = []

for i in range(100):
    
    edad = generar_edad()

    red = generar_red_social(edad)
    
    frecuencia = generar_frecuencia()

    horas = generar_horas(frecuencia)

    sesiones = generar_sesiones(horas)

    contenido = generar_tipo_contenido(red)

    interaccion = generar_interaccion(horas)

    publica = generar_publica_contenido(
        interaccion, horas,
        sesiones, red, contenido
    )

    uso_noche = generar_uso_nocturno(horas)

    notificaciones_usuario = generar_notificaciones(
        horas, sesiones, interaccion
    )

    motivo = generar_motivo(
        red, contenido
    )

    satisfaccion = generar_satisfaccion(
        horas, uso_noche
    )
    
    registro = {
        "edad": edad,
        "red_social_principal": red,
        "frecuencia_uso": frecuencia,
        "horas_diarias": horas,
        "sesiones_diarias": sesiones,
        "tipo_contenido": contenido,
        "interaccion_diaria": interaccion,
        "publica_contenido": publica,
        "uso_nocturno": uso_noche,
        "notificaciones": notificaciones_usuario,
        "motivo_principal": motivo,
        "nivel_satisfaccion": satisfaccion
    }
    
    registro = aplicar_nulls(registro)

    datos.append(registro)


#TODO: Crear DataFrame:
df = pd.DataFrame(datos)

#TODO: Guardar el DataFrame como CSV:
df.to_csv(
    "redes_sociales_test.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Dataset creado correctamente.")
print(f"Registros: {len(df)}")
print(f"Columnas: {len(df.columns)}")