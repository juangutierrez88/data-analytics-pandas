import pandas as pd
import os

# manipular archivo csv creado en la práctica #1

csv_file = "ventas.csv"

if os.path.exists(csv_file):
    print(f'Archivo {csv_file} existe')

    csv_file_size = os.path.getsize(csv_file)
    print(f'Tamaño de archivo: {csv_file_size} bytes')

else:
    print(f'Archivo {csv_file} no encontrado')
    exit()

# Lectura de archivo
df = pd.read_csv(csv_file)

# Primeras 3 filas
#print('Primeras filas')
#print(df.head(3))

# Últimas filas
#print('Últimas filas')
#print(df.tail(2))
print(df)

# Info del dataframe
print('Información DataFrame')
print(df.info())

# Estadistica descriptiva
print('Datos estadísticos descriptivos')
print(df.describe())

# Identificar columnas
print('Columnas disponibles:')
for i, column in enumerate(df.columns,1):
    print(f'{i}. {column}')

# Obtener dimensiones del dataframe
rows, columns = df.shape
print(f'Dimensiones: {rows} filas x {columns} columnas')

# extraer tipos de datos, ya se incluye dentro de df.info()
print('Tipos de datos')
print(df.dtypes)