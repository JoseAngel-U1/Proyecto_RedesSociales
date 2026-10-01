# #! Funciones:
import random
from variables_categoricas import *

def generar_null(valor, probabilidad=0.10):
    if random.random() < probabilidad:
        return None
    return valor

def aplicar_nulls(registro, probabilidad=0.10):
    for columna in registro:
        registro[columna] = generar_null(
            registro[columna],
            probabilidad
        )

    return registro

def elegir_con_probabilidad(opciones, probabilidades):
    return random.choices(
        opciones,
        weights=probabilidades,
        k=1
    )[0]



#TODO: Generar datos provabilistuicos:
def generar_edad():
    rangos = [
        (13, 17),
        (18, 24),
        (25, 34),
        (35, 44),
        (45, 54)
    ]

    probabilidades = [12, 28, 28, 20, 12]

    rango = elegir_con_probabilidad(
        rangos,
        probabilidades
    )

    return random.randint(rango[0], rango[1])


def generar_red_social(edad):
    if edad <= 17:
        probabilidades = [25, 5, 30, 5, 20, 15]

    elif edad <= 24:
        probabilidades = [25, 5, 25, 10, 20, 15]

    elif edad <= 34:
        probabilidades = [20, 15, 15, 10, 20, 20]

    elif edad <= 44:
        probabilidades = [15, 20, 10, 10, 20, 25]

    else:
        probabilidades = [10, 25, 5, 10, 20, 30]

    return elegir_con_probabilidad(
        red_social_principal,
        probabilidades
    )


def generar_frecuencia():
    probabilidades = [30, 30, 20, 12, 8]

    return elegir_con_probabilidad(
        frecuencia_uso,
        probabilidades
    )


def generar_horas(frecuencia):
    rangos = {
        "Varias veces al día": (3.0, 12.0),
        "Diariamente": (2.0, 8.0),
        "Varias veces por semana": (1.0, 5.0),
        "Semanalmente": (0.5, 3.0),
        "Raramente": (0.5, 1.5)
    }

    minimo, maximo = rangos[frecuencia]

    return round(
        random.uniform(minimo, maximo),
        1
    )


def generar_sesiones(horas):
    if horas <= 1.0:
        minimo, maximo = 1, 5

    elif horas <= 3.0:
        minimo, maximo = 2, 10

    elif horas <= 6.0:
        minimo, maximo = 5, 18

    elif horas <= 9.0:
        minimo, maximo = 8, 25

    else:
        minimo, maximo = 10, 30

    return random.randint(minimo, maximo)


def generar_tipo_contenido(red):
    probabilidades = {
        "Instagram": [25, 5, 8, 7, 5, 15, 25, 10],
        "Facebook": [20, 20, 8, 12, 3, 7, 15, 15],
        "TikTok": [25, 5, 7, 8, 10, 15, 20, 10],
        "X": [15, 40, 10, 10, 3, 5, 10, 7],
        "YouTube": [20, 10, 15, 10, 10, 15, 5, 15],
        "WhatsApp": [20, 15, 8, 8, 3, 12, 20, 14]
    }

    return elegir_con_probabilidad(
        tipo_contenido,
        probabilidades[red]
    )


def generar_interaccion(horas):
    if horas <= 1.0:
        minimo, maximo = 0, 25

    elif horas <= 3.0:
        minimo, maximo = 5, 60

    elif horas <= 6.0:
        minimo, maximo = 20, 110

    elif horas <= 9.0:
        minimo, maximo = 40, 160

    else:
        minimo, maximo = 60, 200

    return random.randint(minimo, maximo)


def generar_publica_contenido(
    interaccion,
    horas,
    sesiones,
    red,
    contenido
):
    probabilidad = 25

    if interaccion <= 25:
        probabilidad -= 10
    elif interaccion >= 61:
        probabilidad += 10

    if interaccion >= 121:
        probabilidad += 5

    if horas > 6:
        probabilidad += 10

    if sesiones > 15:
        probabilidad += 5

    if red in ["Instagram", "TikTok", "YouTube"]:
        probabilidad += 5

    if contenido == "Tutoriales":
        probabilidad += 5

    elif contenido in ["Música", "Videojuegos", "Memes"]:
        probabilidad += 3

    probabilidad = max(5, min(probabilidad, 85))

    return "Sí" if random.random() < probabilidad / 100 else "No"


def generar_uso_nocturno(horas):
    if horas < 2:
        probabilidades = [20, 25, 35, 15, 5]

    elif horas <= 4:
        probabilidades = [10, 20, 35, 25, 10]

    elif horas <= 7:
        probabilidades = [5, 15, 25, 35, 20]

    elif horas <= 9:
        probabilidades = [3, 7, 20, 40, 30]

    else:
        probabilidades = [2, 5, 15, 38, 40]

    return elegir_con_probabilidad(
        uso_nocturno,
        probabilidades
    )

def generar_notificaciones(horas, sesiones, interaccion):

    actividad = (
        horas * 5 +
        sesiones * 2 +
        interaccion
    )

    if actividad < 60:
        probabilidades = [30, 45, 20, 5]

    elif actividad < 120:
        probabilidades = [15, 45, 30, 10]

    elif actividad < 200:
        probabilidades = [5, 30, 45, 20]

    elif actividad < 300:
        probabilidades = [2, 15, 43, 40]

    else:
        probabilidades = [1, 9, 35, 55]

    return elegir_con_probabilidad(
        notificaciones,
        probabilidades
    )


def generar_motivo(red, contenido):

    probabilidades = {
        "Entretenimiento": 30,
        "Comunicación": 25,
        "Información": 15,
        "Educación": 12,
        "Trabajo": 10,
        "Promoción/negocio": 8
    }

    if red == "WhatsApp":
        probabilidades["Comunicación"] += 15

    if red == "X" and contenido == "Noticias":
        probabilidades["Información"] += 15

    if red == "YouTube" and contenido in ["Educación", "Tutoriales"]:
        probabilidades["Educación"] += 15

    if red in ["Instagram", "TikTok"] and contenido == "Memes":
        probabilidades["Entretenimiento"] += 15

    if contenido == "Noticias":
        probabilidades["Información"] += 5

    if contenido in ["Educación", "Tutoriales"]:
        probabilidades["Educación"] += 5

    opciones = list(probabilidades.keys())
    pesos = list(probabilidades.values())

    return elegir_con_probabilidad(
        opciones,
        pesos
    )


def generar_satisfaccion(horas, uso_noche):

    probabilidades = {
        "Muy bajo": 8,
        "Bajo": 15,
        "Medio": 35,
        "Alto": 30,
        "Muy alto": 12
    }

    if horas > 9:
        probabilidades["Muy bajo"] += 4
        probabilidades["Bajo"] += 4
        probabilidades["Alto"] -= 4
        probabilidades["Muy alto"] -= 4

    elif 2 <= horas <= 6:
        probabilidades["Alto"] += 3
        probabilidades["Muy alto"] += 2
        probabilidades["Bajo"] -= 3
        probabilidades["Muy bajo"] -= 2

    if uso_noche == "Siempre":
        probabilidades["Muy bajo"] += 3
        probabilidades["Bajo"] += 2
        probabilidades["Alto"] -= 3
        probabilidades["Muy alto"] -= 2

    opciones = list(probabilidades.keys())
    pesos = list(probabilidades.values())

    return elegir_con_probabilidad(
        opciones,
        pesos
    )