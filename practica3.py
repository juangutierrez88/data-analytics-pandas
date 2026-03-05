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

# Filtro por producto
print('Ventas de un producto')
df_product = df[df['Producto'] == 'Laptop']
print(df_product[['Fecha','Cantidad', 'Total']].to_string(index=False))

# Filtrar multiples condiciones

# Uso de operador AND (&)
print('Ventas de Laptop en Enero')
condicion1 = df['Producto'] == 'Laptop'
condicion2 = df['Cantidad'] > 5
df_laptop_mayor_5 = df[condicion1 & condicion2]

if len(df_laptop_mayor_5) > 0:
    print(df_laptop_mayor_5[['Fecha', 'Cantidad', 'Total']].to_string(index=False))
else:
    print('No se encontraron ventas de Laptop con cantidad mayor a 5')

# Uso de operador OR (|)
print('Ventas de teclado o tablet')
condicion3 = df['Producto'] == 'Teclado'
condicion4 = df['Producto'] == 'Tablet'
df_teclado_tablet = df[condicion3 | condicion4]

if len(df_teclado_tablet) > 0:
    print(df_teclado_tablet[['Fecha', 'Producto', 'Cantidad', 'Total']].to_string(index=False))
else:
    print('No se encontraron ventas de teclado o tablet')

# Filtro por rango de fechas
print('Ventas en Enero 2024, después del 2 de Enero')
df_despues_enero2 = df[df['Fecha'] > '2024-01-02']
print(df_despues_enero2[['Fecha', 'Producto', 'Cantidad', 'Total']].to_string(index=False))

# Ventas totales
total_ingresos = df['Total'].sum()
print(f'Ingresos totales: ${total_ingresos:.2f}')

# Promedio de ventas
promedio_ventas = df['Total'].mean()
print(f'Promedio de ventas: ${promedio_ventas:.2f}')

# Producto más vendido
mas_vendido = df.loc[df['Cantidad'].idxmax()]
print(f"Producto más vendido: {mas_vendido['Producto']} ({mas_vendido['Cantidad']} unidades)")

# Día de mayor venta
dia_prime_ventas = df.loc[df['Total'].idxmax()]
print(f"Día de mayor venta: {dia_prime_ventas['Fecha'].strftime('%Y-%m-%d')} (Total: ${dia_prime_ventas['Total']:.2f})")

# Exportar datos filtrados a nuevo CSV
df_laptop_mayor_5.to_csv('ventas_laptop_mayor_5.csv', index=False)
print('Datos de ventas de Laptop con cantidad mayor a 5 guardados')

# Producto de mayores ventas
df_product.to_csv('ventas_producto_estrella.csv', index=False)
print('Datos de ventas del producto estrella guardados')

# Dia más productivo
dia_prime_ventas.to_csv('ventas_dia_productivo.csv', index=False)
print('Datos del día más productivo guardados')

# Guardar df con nuevas columnas
df.to_csv('ventas_modificado.csv', index=False)
print('Datos con nuevas columnas guardados en ventas_modificado.csv')