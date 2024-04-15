import pandas as pd
data = pd.read_csv('data.csv')


def convert_wage(wage):
    if wage[-1] == 'K':
        return float(wage[1:-1]) * 10**3
    elif wage[-1] == 'M':
        return float(wage[1:-1]) * 10**6
    else:
        return float(wage[1:])


data['Wage'] = data['Wage'].apply(convert_wage)


club_salaries = data.groupby('Club')['Wage'].sum()

top_clubs = club_salaries.sort_values(ascending=False)

print(top_clubs.head(10))
