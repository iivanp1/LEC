import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')


def convert_value(value):
    if value[-1] == 'K':
        return float(value[1:-1]) * 10**3
    elif value[-1] == 'M':
        return float(value[1:-1]) * 10**6
    else:
        return float(value[1:])


data['Value'] = data['Value'].apply(convert_value)


fig, ax = plt.subplots()


ax.scatter(data['Overall'], data['Value'])

ax.set_title('Valor de los jugadores en función de su valoración')
ax.set_xlabel('Valoración (Overall)')
ax.set_ylabel('Valor')


plt.show()
