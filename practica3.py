import pandas as pd
import os

# Cargar datos
csv_file = 'ventas.csv'
if not os.path.exists(csv_file):
    print(f'Archivo {csv_file} no encontrado')
    exit()

df = pd.read_csv(csv_file)
print(f'Dimensiones originales: {df.shape}')

# Exhibir datos originales
print('Datos originales:')
print(df.to_string(index=False))

# Identificar tipo actual
print(f"Tipo actual de Fecha: {df['Fecha'].dtype}")

# Modificación de tipo a datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])
print(f"Nuevo tipo para Fecha: {df['Fecha'].dtype}")

# mostrar conversión
print('Fechas modificadas correctamente:')
print(df[['Fecha', 'Producto']].head())

# Creación de nuevas columnas
df['Año'] = df['Fecha'].dt.year
df['Mes'] = df['Fecha'].dt.month
df['Día'] = df['Fecha'].dt.day
df['Día_semana'] = df['Fecha'].dt.day_name() # Monday, Tuesday,...

print('Nuevas columnas añadidas:')
print(df[['Fecha', 'Año', 'Mes', 'Día', 'Día_semana', 'Producto']].to_string(index=False))

# Filtro de cantidades mayor a 5
df_mayor_5 = df[df['Cantidad'] > 5]
print('stock mayor a 5')
print(df_mayor_5[['Producto','Cantidad', 'Total']].to_string(index=False))

# Filtro pro producto
print('Ventas de un producto')
df_product = df[df['Producto'] == 'Laptop']
print(df_product[['Fecha','Cantidad', 'Total']].to_string(index=False))