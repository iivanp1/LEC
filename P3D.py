import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv')

data = data.dropna(subset=['SprintSpeed'])


X = data['Acceleration'].values.reshape(-1, 1)  
y = data['SprintSpeed']


x = data['Acceleration']
n = len(x)
sum_xy = np.sum(x*y)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)


intercept = sum_y/n - slope*(sum_x/n)


fig, ax = plt.subplots()


ax.scatter(data['Acceleration'], data['SprintSpeed'])


x = np.linspace(data['Acceleration'].min(), data['Acceleration'].max(), 100)
y = slope * x + intercept
ax.plot(x, y, color='red')

ax.set_title('Velocidad en función de la aceleración')
ax.set_xlabel('Aceleración')
ax.set_ylabel('Velocidad')


plt.show()
