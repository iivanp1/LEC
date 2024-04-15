import pandas as pd

df = pd.read_csv('data.csv')

estratificacion_equipo = df.groupby('Club')
valoracion = estratificacion_equipo['Overall'].mean()
velocidad = estratificacion_equipo['SprintSpeed'].mean()
marcaje = estratificacion_equipo['Marking'].mean()

top_valoracion = valoracion.nlargest(5).reset_index()
top_velocidad = velocidad.nlargest(5).reset_index()
top_marcaje = marcaje.nlargest(5).reset_index()

tabla_valoracion = pd.DataFrame({'Club': top_valoracion['Club'], 'Valoración Media': top_valoracion['Overall']})
tabla_velocidad = pd.DataFrame({'Club': top_velocidad['Club'], 'Velocidad Media': top_velocidad['SprintSpeed']})
tabla_marcaje = pd.DataFrame({'Club': top_marcaje['Club'], 'Marcaje Media': top_marcaje['Marking']})

print(tabla_valoracion)

print(tabla_velocidad)

print(tabla_marcaje)
