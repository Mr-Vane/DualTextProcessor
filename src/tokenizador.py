import csv
import re
import os
import json

tokens = {}

SPECIAL_TOKENS = {
    '<pad>': 0,
    '<bos>': 1,
    '<eos>': 2,
    '<unk>': 3
}

def escribir_dataset(linea_entrada, linea_salida, columna1, columna2):
    file_exists = os.path.isfile("data/database/dataset_tokenizado.csv")
    
    with open("data/database/dataset_tokenizado.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([columna1, columna2])
        writer.writerow([linea_entrada, linea_salida])


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
        for row in reader:
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
            
            escribir_dataset(linea_token_entrada, linea_token_salida, columna1, columna2)
