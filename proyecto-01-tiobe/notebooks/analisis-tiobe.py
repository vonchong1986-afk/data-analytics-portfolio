"""
Análisis del índice TIOBE - Septiembre 2026
Proyecto 01 - Data Analytics Portfolio
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# 1. Cargar datos
ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'data', 'tiobe-2026.csv')
df = pd.read_csv(ruta_csv)

print("=== DATOS CARGADOS ===")
print(df)
print()

# 2. Análisis descriptivo
print("=== ANÁLISIS DESCRIPTIVO ===")
print(f"Lenguaje líder: {df.iloc[0]['lenguaje']} con {df.iloc[0]['rating']}%")
print(f"Rating total del top 7: {df['rating'].sum():.2f}%")
print(f"Rating promedio: {df['rating'].mean():.2f}%")
print()

# 3. Lenguajes que subieron vs bajaron
subieron = df[df['cambio'] > 0]['lenguaje'].tolist()
bajaron = df[df['cambio'] < 0]['lenguaje'].tolist()

print(f"Lenguajes que subieron: {subieron}")
print(f"Lenguajes que bajaron: {bajaron}")
print()

# 4. Gráfico de ratings
plt.figure(figsize=(10, 6))
colores = ['#3776AB' if l == 'Python' else '#888888' for l in df['lenguaje']]
plt.barh(df['lenguaje'], df['rating'], color=colores)
plt.xlabel('Rating (%)')
plt.title('Top 7 lenguajes de programación - TIOBE Septiembre 2026')
plt.gca().invert_yaxis()
plt.tight_layout()

ruta_grafico = os.path.join(os.path.dirname(__file__), '..', 'images', 'grafico-top7.png')
plt.savefig(ruta_grafico, dpi=100)
print(f"Gráfico guardado en: {ruta_grafico}")

# 5. Gráfico de cambios
plt.figure(figsize=(10, 6))
colores_cambio = ['#2ca02c' if c > 0 else '#d62728' for c in df['cambio']]
plt.barh(df['lenguaje'], df['cambio'], color=colores_cambio)
plt.xlabel('Cambio respecto al año anterior (%)')
plt.title('Cambio anual en rating - TIOBE Septiembre 2026')
plt.axvline(0, color='black', linewidth=0.8)
plt.gca().invert_yaxis()
plt.tight_layout()

ruta_grafico2 = os.path.join(os.path.dirname(__file__), '..', 'images', 'grafico-cambios.png')
plt.savefig(ruta_grafico2, dpi=100)
print(f"Gráfico guardado en: {ruta_grafico2}")

print()
print("=== ANÁLISIS COMPLETADO ===")

