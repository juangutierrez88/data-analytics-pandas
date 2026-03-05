# crear_datos_logistica.py para la práctica 4
import pandas as pd
import os

# Asegurar que la carpeta existe
os.makedirs('logistica', exist_ok=True)

# Datos de rutas de entrega
datos_rutas = {
    'id_ruta': ['R001', 'R002', 'R003', 'R004', 'R005', 'R006'],
    'fecha': ['2024-01-15', '2024-01-15', '2024-01-16', '2024-01-16', '2024-01-17', '2024-01-17'],
    'origen': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona', 'Madrid'],
    'destino': ['Barcelona', 'Madrid', 'Valencia', 'Alicante', 'Sevilla', 'Bilbao'],
    'distancia_km': [620, 620, 350, 180, 850, 395],
    'tiempo_min': [390, 405, 210, 115, 540, 250],
    'combustible_litros': [45.5, 46.2, 26.8, 14.2, 62.5, 29.8],
    'camionero': ['Carlos', 'Ana', 'Carlos', 'Luis', 'Ana', 'Carlos']
}

df_logistica = pd.DataFrame(datos_rutas)
df_logistica.to_csv('logistica/entregas_2024_q1.csv', index=False)
print("Archivo creado: logistica/entregas_2024_q1.csv")
print(df_logistica)
