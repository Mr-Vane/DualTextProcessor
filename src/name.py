import csv

def leer_columnas_csv(archivo):
    with open(archivo, 'r', newline='', encoding='utf-8') as file:
        lector = csv.reader(file)
        primera_linea = next(lector)  # Lee solo la primera línea
        
        # Verificar que hay al menos 2 columnas
        if len(primera_linea) >= 2:
            columna1 = primera_linea[0]
            columna2 = primera_linea[1]
            return columna1, columna2
        else:
            print("El archivo no tiene al menos 2 columnas")
            return None, None
