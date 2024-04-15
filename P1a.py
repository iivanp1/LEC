import pandas as pd
import matplotlib.pyplot as plt

archivo_csv = 'data.csv'
df = pd.read_csv(archivo_csv)


paises_con_jugadores = df['Nationality'].nunique()
print(f'Hay {paises_con_jugadores} países que poseen al menos un jugador.')



jugadores_pais = df['Nationality'].value_counts()


top_15_paises = jugadores_pais.head(15)
otros_paises = jugadores_pais[15:].sum()


porcentaje_top_15 = (top_15_paises.sum() / df.shape[0]) * 100
print(f'Los 15 países con más jugadores abarcan el {porcentaje_top_15:.2f}% del total de jugadores.')



top_paises_df = pd.DataFrame(top_15_paises).reset_index()
top_paises_df.columns = ['Nacionalidad', 'Número de Jugadores']
otros_paises_df = pd.DataFrame({'Nacionalidad': ['Otros países'], 'Número de Jugadores': [otros_paises]})
combined_df = pd.concat([top_paises_df, otros_paises_df])


plt.figure(figsize=(8, 8))
plt.pie(combined_df['Número de Jugadores'], labels=combined_df['Nacionalidad'], autopct='%1.1f%%', startangle=140)
plt.title('Cantidad de jugadores por país')
plt.show()
