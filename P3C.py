import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data.csv')
def convert_height(height):
    if isinstance(height, str):
        feet, inches = map(int, height.split('\''))
        return (feet * 12 + inches) * 2.54
    else:
        return height


def convert_weight(weight):
    if isinstance(weight, str):
        pounds = int(weight[:-3])
        return pounds * 0.453592
    else:
        return weight


data['Height'] = data['Height'].apply(convert_height)
data['Weight'] = data['Weight'].apply(convert_weight)

columns = ['Height', 'Weight', 'Agility', 'Strength', 'SprintSpeed', 'Acceleration', 'HeadingAccuracy', 'Dribbling', 'BallControl']

corr_matrix = data[columns].corr()


plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True, square=True)

plt.title('Matriz de correlación')
plt.show()
