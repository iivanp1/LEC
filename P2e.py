import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv')

def convert_wage(wage):
    if wage[-1] == 'K':
        return float(wage[1:-1]) * 10**3
    elif wage[-1] == 'M':
        return float(wage[1:-1]) * 10**6
    else:
        return float(wage[1:])

data['Wage'] = data['Wage'].apply(convert_wage)


club1 = 'FC Barcelona'  
club2 = 'Chelsea'  

data_club1 = data[data['Club'] == club1]['Wage'].dropna().astype(float)
data_club2 = data[data['Club'] == club2]['Wage'].dropna().astype(float)

fig, ax = plt.subplots()

ax.boxplot([data_club1, data_club2], labels=[club1, club2], notch=True, patch_artist=True)

ax.set_title('Comparación de los salarios de los jugadores')
ax.set_xlabel('Club')
ax.set_ylabel('Salario')

plt.show()
