import re
import pandas as pd

def ingest_data():
    # Leer el archivo y procesar las líneas
    with open("clusters_report.txt", "r") as file:
        lineas = file.readlines()

    # Procesar los títulos combinando las dos primeras líneas
    titulos_completos = []
    for idx in range(2):  # Solo para las dos primeras líneas
        titulos_completos.append(re.sub(r"\s{2,}", "-", lineas[idx]).strip().split("-"))

    # Ajustar las posiciones de los títulos
    titulos_completos[0].pop()
    titulos_completos[1].pop(0)

    # Unir los títulos correspondientes
    titulos = [
        titulos_completos[0][0], 
        f"{titulos_completos[0][1]} {titulos_completos[1][0]}",
        f"{titulos_completos[0][2]} {titulos_completos[1][1]}",
        titulos_completos[0][3]
    ]

    # Inicializar el diccionario de datos
    data = {titulo.lower().replace(" ", "_"): [] for titulo in titulos}

    # Procesar las líneas de datos
    for linea in lineas[2:]:
        fragmentos = re.sub(r"\s{2,}", ".", linea).strip().split(".")
        fragmentos = list(filter(None, fragmentos))  # Eliminar entradas vacías

        if fragmentos and fragmentos[0].isnumeric():
            data["cluster"].append(int(fragmentos[0]))
            data["cantidad_de_palabras_clave"].append(int(fragmentos[1]))
            data["porcentaje_de_palabras_clave"].append(float(fragmentos[2][:-2].replace(",", ".")))
            data["principales_palabras_clave"].append(" ".join(fragmentos[3:]))
        elif data["principales_palabras_clave"]:
            data["principales_palabras_clave"][-1] += " " + " ".join(fragmentos)

    # Crear el DataFrame a partir del diccionario procesado
    df = pd.DataFrame(data)

    return df

print(ingest_data())
