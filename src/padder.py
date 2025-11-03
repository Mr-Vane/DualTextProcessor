import csv
import ast
import numpy as np
import os
from tqdm import tqdm

lista_completa = []

def calcular_longitudes_optimas(columna1, columna2):
    longitudes_entrada = []
    longitudes_salida = []
    
    with open("data/database/dataset_tokenizado.csv", newline="", encoding="utf-8") as dataset:
        reader = csv.DictReader(dataset)
        for row in reader:
            entrada = ast.literal_eval(row[columna1])
            salida = ast.literal_eval(row[columna2])
            longitudes_entrada.append(len(entrada))
            longitudes_salida.append(len(salida))
    
    #Percentil 95
    max_entrada = int(np.percentile(longitudes_entrada, 95))
    max_salida = int(np.percentile(longitudes_salida, 95))
    
    print(f"Longitud óptima entrada: {max_entrada}")
    print(f"Longitud óptima salida: {max_salida}")
    
    return max_entrada, max_salida

def aplicar_padding(max_entrada, max_salida,columna1, columna2):
    if os.path.exists("data/database/dataset_tokenizado_padded.csv"):
        os.remove("data/database/dataset_tokenizado_padded.csv")
    
    with open("data/database/dataset_tokenizado.csv", newline="", encoding="utf-8") as dataset:
        reader = csv.DictReader(dataset)
        
        for i, row in enumerate(tqdm(reader, desc="Padding")):
            lista_momentanea = []
            entrada = ast.literal_eval(row[columna1])
            salida = ast.literal_eval(row[columna2])
            
            #Padding
            if len(entrada) < max_entrada:
                entrada = entrada + [0] * (max_entrada - len(entrada))  # padding
            else:
                entrada = entrada[:max_entrada]
            
            if len(salida) < max_salida:
                salida = salida + [0] * (max_salida - len(salida))  # padding
            else:
                salida = salida[:max_salida]

            lista_momentanea.append(entrada)
            lista_momentanea.append(salida)

            lista_completa.append(lista_momentanea)
            
        # Escribir al archivo
        file_exists = os.path.isfile("data/database/dataset_tokenizado_padded.csv")
        with open("data/database/dataset_tokenizado_padded.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow([columna1, columna2])
                for fila in lista_completa:
                    writer.writerow([fila[0], fila[1]])
