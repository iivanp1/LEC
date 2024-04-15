import pandas as pd
archivo_csv = 'data.csv'
df = pd.read_csv(archivo_csv)


paises_con_jugadores = df['Nationality'].nunique()
print(f'Hay {paises_con_jugadores} países que poseen al menos un jugador.')

top_15_paises = df['Nationality'].value_counts().head(15).sum()
porcentaje_top_15 = (top_15_paises / df.shape[0]) * 100
print(f'Los 15 países con más jugadores abarcan el {porcentaje_top_15:.2f}% del total de jugadores.')
