# Código de logística (rutas de entrega)
import pandas as pd
import os

# Lectura de archivo csv
ruta_archivo = os.path.join('logistica', 'entregas_2024_q1.csv')

# verificar existencia del archivo
if not os.path.exists(ruta_archivo):
    print("Archivo no encontrado")
    print("Ejecutar archivo crear_datos_logistica.py")

# Lectura del archivo
df = pd.read_csv(ruta_archivo)
print(f"Datos cargados desde: {ruta_archivo}")
print(f"Dimensiones: {df.shape[0]} rutas x {df.shape[1]} columnas")

# Mostrar los datos, .tail() para ultimos, .head() para los primeros
# incluir .to_string(index=False)
print("Despliegue del contenido del dataframe")
print(df)

print("Información del dataframe")
print(df.info())

# Obtención de estadísticas descriptivas
print("Datos estadísticos")
print(df.describe())

# Sección para limpieza de datos

print("Cambiar formato de fechas")
df['fecha'] = pd.to_datetime(df['fecha'])

print("Creación de columnas de datos compuestos/derivados")
df['velocidad_promedio_kmh'] = (df['distancia_km'] / df['tiempo_min']) * 60
df['eficiencia_combustible'] = df['distancia_km'] / df['combustible_litros']
print("Columnas creadas con exito:")
print(" - velocidad_promedio_kmh (km/h)")
print(" - eficiencia_combustible (km/litro)")

# Extracción de fechas
df['dia_semana'] = df['fecha'].dt.day_name()
df['mes'] = df['fecha'].dt.month
df['dia'] = df['fecha'].dt.day

# Análisis por conductor/camionero

print("\nEstadísticos por camionero")

estadisticas_camioneros = df.groupby('camionero').agg({
    'distancia_km': ['sum', 'mean'],
    'tiempo_min': ['sum', 'mean'],
    'combustible_litros': ['sum', 'mean'],
}).round(2)

print(estadisticas_camioneros)

print("\nNúmero de rutas por camionero")

# Cuenta por camionero, muestra en un orden camionero, cantidad_ruta
rutas_por_camionero = df['camionero'].value_counts()

for camionero, rutas in rutas_por_camionero.items():
    print(f"{camionero}: {rutas} rutas")

# Análisis de rutas más larga y más corta
ruta_max = df.loc[df['distancia_km'].idxmax()]
ruta_min = df.loc[df['distancia_km'].idxmin()]

print(f"\nRuta más larga: {ruta_max['origen']} - {ruta_max['destino']}")
print(f"Distancia: {ruta_max['distancia_km']} km")
print(f"Tiempo: {ruta_max['tiempo_min']} minutos")
print(f"camionero: {ruta_max['camionero']}")

print(f"\nRuta más corta: {ruta_min['origen']} - {ruta_min['destino']}")
print(f"Distancia: {ruta_min['distancia_km']} km")
print(f"Tiempo: {ruta_min['tiempo_min']} minutos")
print(f"camionero: {ruta_min['camionero']}")

# Filtrar rutas largas
rutas_largas = df[df['distancia_km'] > 400]
if len(rutas_largas) > 0:
    for _, ruta in rutas_largas.iterrows():
        print(f" - {ruta['origen']} - {ruta['destino']}: {ruta['distancia_km']} km")
else:
    print("No hay rutas > 400 km")


print("\nAnálisis por origen y destino")
print("Por ciudad de origen:")

origen_counts = df['origen'].value_counts()
for ciudad, count in origen_counts.items():
    print(f"- {ciudad}: {count} rutas")

print("\nRuta más frecuente")
ruta_mas_frecuente = df.groupby(['origen', 'destino']).size().sort_values(ascending=False)
for (origen,destino), count in ruta_mas_frecuente.items():
    print(f" - {origen} - {destino}: {count} veces")


print("\nEficiencia por camionero") # ¿Quién tiene mayor rendimiento?
eficiencia_por_camionero = df.groupby('camionero')['eficiencia_combustible'].mean().round(2)
print("Promedio por camionero (km/litro):")
for camionero, eficiencia in eficiencia_por_camionero.items():
    print(f" - {camionero}: {eficiencia} km/l")

promedio_eficiencia = df['eficiencia_combustible'].mean()
print(f"\nPromedio general de eficiencia: {promedio_eficiencia:.2f} km/l")

# Rutas ineficientes (debajo del promedio)
rutas_ineficientes = df[df['eficiencia_combustible'] < promedio_eficiencia]
if len(rutas_ineficientes) > 0:
    for _,ruta in rutas_ineficientes.iterrows():
        print(f"- {ruta['origen']} - {ruta['destino']}: {ruta['eficiencia_combustible']:.2f} km/l")
else:
    print("\nTodas las rutas son eficientes")

# Exportar resultados
os.makedirs('logistica/reportes', exist_ok=True)

df.groupby('camionero').agg({
    'distancia_km':'sum',
    'tiempo_min':'sum',
    'combustible_litros':'sum'
}).round(2).to_csv('logistica/reportes/rutas_largas.csv',index=False)
print("reportes/rutas_largas.csv guardado")

# guardar dataset enriquecido
df.to_csv('logistica/reportes/rutas_completo.csv', index=False)
print("reportes/rutas_completo.csv guardado")