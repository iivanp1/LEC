import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
archivo_csv = 'data.csv'
df = pd.read_csv(archivo_csv)
df['Penalties'] = pd.to_numeric(df['Penalties'], errors='coerce')

percentile_90 = df['Overall'].quantile(0.9)

player_90 = df[df['Overall'] > percentile_90]

penalties_value = player_90['Penalties'].max()

print(f"La valoración en penalties del jugador que tiene más valoración que el 90% de los jugadores es {penalties_value}")

players_above_85 = df[df['Penalties'] > 85]
percentage = (len(players_above_85) / len(df)) * 100

print(f"El {percentage}% de los jugadores tiene más de 85 de valoración en penalties")
