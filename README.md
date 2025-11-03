# DualTextProcessor

## 📝 Descripción del Proyecto

**DualTextProcessor** es una herramienta de procesamiento de lenguaje natural (PLN) escrita en Python, diseñada para preparar conjuntos de datos de texto bilingües o de doble columna para su uso en modelos de *Machine Learning* o *Deep Learning*, como los modelos de traducción automática o *Sequence-to-Sequence*.

El proyecto automatiza dos pasos cruciales en el preprocesamiento de datos:

1. **Tokenización**: Convierte las palabras de las columnas de texto en secuencias de tokens numéricos, creando un vocabulario y un mapeo de tokens.

1. **Padding**: Aplica relleno (padding) a las secuencias tokenizadas para asegurar que todas las entradas y salidas tengan una longitud uniforme, lo cual es un requisito común para el entrenamiento de redes neuronales recurrentes (RNN) o transformadores.

## 🚀 Características Principales

- **Procesamiento de Doble Columna**: Diseñado específicamente para manejar conjuntos de datos con dos columnas de texto (por ejemplo, idioma de origen e idioma de destino).

- **Generación de Vocabulario**: Crea un vocabulario único y guarda los mapeos de palabras a tokens (`tokens.json`) y de tokens a palabras (`token_to_word.json`).

- **Tokens Especiales**: Incluye tokens especiales esenciales para modelos de secuencia:
  - `<pad>`: Relleno (Token 0)
  - `<bos>`: Inicio de secuencia (Token 1)
  - `<eos>`: Fin de secuencia (Token 2)
  - `<unk>`: Palabra desconocida (Token 3)

- **Longitud Óptima**: Calcula las longitudes de secuencia óptimas para el padding basándose en la distribución de los datos.

- **Salida Estructurada**: Genera archivos CSV con los datos tokenizados y con padding, listos para ser cargados en un *framework* de *Deep Learning*.



## 🛠️ Instalación

### Requisitos

Asegúrate de tener Python instalado en tu sistema.

```bash
pip install -r requirements.txt
```

### Estructura del Proyecto

El proyecto tiene la siguiente estructura de directorios:

```
DualTextProcessor/
├── data/
│   ├── database/             # Contiene los datasets procesados
│   ├── tokens/               # Contiene los archivos de mapeo de tokens
├── src/                      # Módulos principales del procesador
│   ├── name.py               # Lógica para la lectura de CSV
│   ├── padder.py             # Lógica para el cálculo y aplicación de padding
│   └── tokenizador.py        # Lógica para la tokenización y creación de vocabulario
├── main.py                   # Punto de entrada principal
└── requirements.txt          # Dependencias del proyecto
```



## 💻 Uso

### 1. Preparación del Dataset

Coloca tu archivo CSV de entrada (con las dos columnas de texto a procesar) en el directorio raíz del proyecto o asegúrate de proporcionar la ruta correcta.

### 2. Ejecución

Ejecuta el script principal `main.py` proporcionando el nombre de tu archivo de base de datos como argumento.

```bash
python main.py <nombre_de_tu_dataset.csv>
```

**Ejemplo:**

Si tu archivo se llama `mi_dataset.csv`, el comando sería:

```bash
python main.py mi_dataset.csv
```

### 3. Salida

Tras la ejecución, se generarán los siguientes archivos en el directorio `data/database/`:

- `dataset_tokenizado.csv`: El dataset con las columnas de texto reemplazadas por secuencias de tokens numéricos.

- `dataset_tokenizado_padded.csv`: El dataset final con las secuencias tokenizadas y con padding aplicado, listo para el entrenamiento.

Además, se crearán los archivos de mapeo de vocabulario en `data/tokens/`:

- `tokens.json`: Mapeo de palabra a token (`word_to_token`).

- `token_to_word.json`: Mapeo de token a palabra (`token_to_word`).



## ⚙️ Módulos Internos

| Archivo | Descripción |
| --- | --- |
| `main.py` | Orquesta el flujo de trabajo: lee el dataset, llama al tokenizador, calcula las longitudes óptimas y aplica el padding. |
| `src/tokenizador.py` | Contiene la lógica para iterar sobre el dataset, construir el vocabulario y convertir las palabras en tokens numéricos. |
| `src/padder.py` | Implementa las funciones para determinar la longitud máxima de las secuencias y aplicar el relleno (`<pad>`) a las secuencias tokenizadas. |
| `src/name.py` | Funciones auxiliares, principalmente para la lectura y manejo de las columnas del archivo CSV de entrada. |

## 🤝 Contribuciones

Cualquier contribucion es bienvenida.
