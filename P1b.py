import pandas as pd
archivo_csv = 'data.csv'
df = pd.read_csv(archivo_csv)

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

media = df['Age'].mean()
desviacion_estandar = df['Age'].std()

print(f'La media de las edades es: {media}')
print(f'La desviación estándar de las edades es: {desviacion_estandar}')
