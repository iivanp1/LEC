import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv')
fig, ax = plt.subplots()

ax.scatter(data['Age'], data['Potential'])

ax.set_title('Potencial de los jugadores en función de su edad')
ax.set_xlabel('Edad')
ax.set_ylabel('Potencial')


plt.show()
