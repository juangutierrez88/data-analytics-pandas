# 1er Script con pandas.
import pandas as pd

# Crear datos desde cero.
datos_ventas = {
    'Fecha': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Producto': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Teclado'],
    'Precio': [1200, 800, 400, 300, 100],
    'Cantidad': [10, 20, 15, 5, 25]
}

# Creación del dataframe, a partir de los datos
df = pd.DataFrame(datos_ventas)
# Mostrar el dataframe
print("DataFrame de Ventas:")
print(df)

# Calcular el total de ventas por cada producto
df['Total'] = df['Cantidad'] * df['Precio']
print("Columa 'Total' Agregada")
print(df)
print()

# Guardar en CSV
archivo_csv = 'ventas.csv'
df.to_csv(archivo_csv, index=False)
print(f"DataFrame guardado en {archivo_csv}")

# Comprobar contenido mediante read_csv
df_leido = pd.read_csv(archivo_csv)
print('\n Contenido del archivo guardado:')
print(df_leido)