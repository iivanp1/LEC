import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

archivo_csv = 'data.csv'
df = pd.read_csv(archivo_csv)

# Estadísticas para 'Overall'
df['Overall'] = pd.to_numeric(df['Overall'], errors='coerce')
overall_stats = df['Overall'].describe()


value_stats = df['Value'].replace({'€': '', 'M': '', 'K': '*1e-3'},regex=True).map(pd.eval)

print("Estadísticas para Overall:\n", overall_stats)
print("\nEstadísticas para Value:\n", value_stats.describe())


plt.figure(figsize=(10, 6))
sns.histplot(df['Overall'], kde=True)
plt.title('Histograma de Overall')
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(value_stats, kde=True)
plt.title('Histograma de Value (En millones)')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Overall'])
plt.title('Boxplot de Overall')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x=value_stats)
plt.title('Boxplot de Value (En millones)')
plt.show()

