"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import re
import pandas as pd

def title_format(header):
    return header.lower().replace(" ", "_")

def ingest_data():

    with open("clusters_report.txt", "r") as file:
        lineas = file.readlines()

    title1 = re.sub(r"\s{2,}", "-", lineas[0]).strip().split("-")
    title2 = re.sub(r"\s{2,}", "-", lineas[1]).strip().split("-")
    title1.pop()
    title2.pop(0)
    titles = [title1[0], title1[1] + " " + title2[0], title1[2] + " " + title2[1], title1[3]]

    data = {title_format(title): [] for title in titles}

    for linea in lineas[2:]:
        linea = re.sub(r"\s{2,}", ".", linea).strip().split(".")
        linea = list(filter(lambda x: x, linea))

        if linea and linea[0].isnumeric():
            cluster = int(linea[0])
            cantidad_palabras = int(linea[1])
            porcentaje_palabras = float(linea[2][:-2].replace(",", "."))
            palabras_clave = " ".join(linea[3:])
            data["cluster"].append(cluster)
            data["cantidad_de_palabras_clave"].append(cantidad_palabras)
            data["porcentaje_de_palabras_clave"].append(porcentaje_palabras)
            data["principales_palabras_clave"].append(palabras_clave)
        elif data["principales_palabras_clave"]:
            line = data["principales_palabras_clave"].pop() + " " + " ".join(linea)              
            data["principales_palabras_clave"].append(line.strip())

    df = pd.DataFrame(data)
    return df

#print(ingest_data())