import pandas as pd

df = pd.read_csv('data.csv')

estratificacion_posicion= df.groupby('Position')

gk = estratificacion_posicion.get_group('GK')
st = estratificacion_posicion.get_group('ST')
lw = estratificacion_posicion.get_group('LW')
cm = estratificacion_posicion.get_group('CM')
cb = estratificacion_posicion.get_group('CB')

gk_media = gk['Dribbling'].mean()
st_media = st['Dribbling'].mean()
lw_media = lw['Dribbling'].mean()
cm_media = cm['Dribbling'].mean()
cb_media = cb['Dribbling'].mean()

gk_varianza = gk['Dribbling'].var()
st_varianza = st['Dribbling'].var()
lw_varianza = lw['Dribbling'].var()
cm_varianza = cm['Dribbling'].var()
cb_varianza = cb['Dribbling'].var()


resultado = pd.DataFrame({'Media dribbling': [gk_media,st_media, lw_media, cm_media, cb_media ], 'Varianza dribbling': [gk_varianza,st_varianza,lw_varianza,cm_varianza,cb_varianza]}, index=['GK','ST','LW','CM','CB'])

print(resultado)
