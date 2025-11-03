import sys
import time

from src.tokenizador import tokenizar
from src.name import leer_columnas_csv
import src.padder

inicio = time.perf_counter()

tokens = {}
indice_token = 1

# Tokens especiales
SPECIAL_TOKENS = {
    '<pad>': 0,
    '<bos>': 1,
    '<eos>': 2,
    '<unk>': 3
}

def main():

    if len(sys.argv) < 2:
        print("You must enter database\n- python main.py <database-name>")
        return
    
    #Nombre del archivo
    dataset_name = sys.argv[1]

    #Leer primera row
    columna1, columna2 = leer_columnas_csv(dataset_name)
    
    print(f"[INFO] Iniciando tokenizacion del archivo: {dataset_name}")
    print(f"[INFO] Columnas a tokenizar: {columna1}, {columna2}")
    #Tokenizamos database
    tokenizar(dataset_name, indice_token, columna1, columna2)

    #Calculamos padding
    print("[INFO] Calculando tamaños padding...")
    max_entrada, max_salida = src.padder.calcular_longitudes_optimas(columna1, columna2)
    print(f"[INFO] Tamaño {columna1}: {max_entrada} | Tamaño {columna2}: {max_salida}")
    #Ejecutamos padding
    src.padder.aplicar_padding(max_entrada, max_salida, columna1, columna2)

    print(f"[TERMINADO]")
    fin = time.perf_counter()
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

if __name__ == "__main__":
    main()
