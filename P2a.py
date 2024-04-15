import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

plt.figure(figsize=(10,6))
sns.boxplot(x='Age', y='Overall', data=df)
plt.title('Análisis exploratorio de las valoraciones estratificado por Edad')
plt.show()
plt.figure(figsize=(10,6))
sns.boxplot(x='Preferred Foot', y='Overall', data=df)
plt.title('Análisis exploratorio de las valoraciones estratificado por Pie Hábil')
plt.show()
