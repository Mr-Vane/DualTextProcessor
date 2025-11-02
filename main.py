import sys

from src.tokenizador import tokenizar
from src.name import leer_columnas_csv
import src.padder

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
        
    #Tokenizamos database
    print("TOKENIZAZADOR")
    tokenizar(dataset_name, indice_token, columna1, columna2)

    #Calculamos padding
    print("PADDER")
    max_entrada, max_salida = src.padder.calcular_longitudes_optimas(columna1, columna2)

    #Ejecutamos padding
    src.padder.aplicar_padding(max_entrada, max_salida, columna1, columna2)


if __name__ == "__main__":
    main()