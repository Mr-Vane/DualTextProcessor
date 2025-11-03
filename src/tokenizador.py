import csv
import re
import os
import json
from tqdm import tqdm
import time

tokens = {}
lista_linea_token = []

inicio = time.perf_counter()

SPECIAL_TOKENS = {
    '<pad>': 0,
    '<bos>': 1,
    '<eos>': 2,
    '<unk>': 3
}

def escribir_dataset(lista_linea_token, columna1, columna2):
    print(f"[INFO] Escribiendo dataset tokenizado en data/database/dataset_tokenizado.csv")
    print(f"[INFO] Escribiendo vocabulario en data/tokens/tokens.json y data/tokens/token_to_word.json")
    file_exists = os.path.isfile("data/database/dataset_tokenizado.csv")
    
    with open("data/database/dataset_tokenizado.csv", "a"   , newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([columna1, columna2])
        for fila in lista_linea_token:
            writer.writerow([str(fila[0]), str(fila[1])])

    with open("data/tokens/tokens.json", "w", encoding="utf-8") as f:
        json.dump(tokens, f, ensure_ascii=False, indent=2)

    token_to_word = {v: k for k, v in tokens.items()}
    with open("data/tokens/token_to_word.json", "w", encoding="utf-8") as f:
        json.dump(token_to_word, f, ensure_ascii=False, indent=2)

# Inicializar con tokens especiales
tokens.update(SPECIAL_TOKENS)
indice_token = len(SPECIAL_TOKENS)

def tokenizar(dataset_name, indice_token, columna1, columna2):
    with open(dataset_name, newline="", encoding="utf-8") as dataset:
        reader = csv.DictReader(dataset)
        for row in tqdm(reader, desc="Tokenizando", unit="línea"):
            lista_linea_actual = []
            entrada = row[columna1].strip()
            salida = row[columna2].strip()

            palabras_entrada = re.findall(r"[\w]+|[.,!?;:]", entrada.lower())
            palabras_salida = re.findall(r"[\w]+|[.,!?;:]", salida.lower())
            
            linea_token_entrada = [SPECIAL_TOKENS['<bos>']]  # Inicio de secuencia
            linea_token_salida = [SPECIAL_TOKENS['<bos>']]  # Inicio de secuencia

            for palabra in palabras_entrada:
                if palabra not in tokens:
                    tokens[palabra] = indice_token
                    indice_token += 1
                linea_token_entrada.append(tokens[palabra])
            
            for palabra in palabras_salida:
                if palabra not in tokens:
                    tokens[palabra] = indice_token
                    indice_token += 1
                linea_token_salida.append(tokens[palabra])
            
            # Añadir token de fin de secuencia
            linea_token_entrada.append(SPECIAL_TOKENS['<eos>'])
            linea_token_salida.append(SPECIAL_TOKENS['<eos>'])

            lista_linea_actual.append(linea_token_entrada)
            lista_linea_actual.append(linea_token_salida)

            lista_linea_token.append(lista_linea_actual)
        
        escribir_dataset(lista_linea_token, columna1, columna2)
