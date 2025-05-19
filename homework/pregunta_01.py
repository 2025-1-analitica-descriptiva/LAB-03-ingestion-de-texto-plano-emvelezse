"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    # Leer el archivo como texto
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
      lines = file.readlines()

    lines = [line.strip() for line in lines if line.strip() and not set(line.strip()).issubset(set('-'))]  

    lines  = lines[2:]
    table = []
    registry = {}

    for line in lines:
      if line[0].isdigit():
        if registry:
            table.append(registry)
        parts = line.split()
        cluster = int(parts[0])
        cant_key_word = int(parts[1])
        percent_key_word = float(parts[2].replace(",", "."))
        principal_key_word = " ".join(parts[4:])
        registry = {
            "cluster":cluster,
            "cantidad_de_palabras_clave":cant_key_word,
            "porcentaje_de_palabras_clave":percent_key_word,
            "principales_palabras_clave":principal_key_word
        }
      else:
          parts = line.split()
          principal_key_word = " ".join(parts)
          registry["principales_palabras_clave"] = registry["principales_palabras_clave"]+  " " + principal_key_word.replace(".", "")
    
    if registry:
       table.append(registry)

    df = pd.DataFrame(table)
    return df
