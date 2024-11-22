import pandas as pd
import numpy as np
import os
from functools import reduce

# Creacion de contratos_df
contratos_df = pd.read_csv(os.path.join('data', 'contratos.csv'))
posibles_categoricos = ('REGIONGEOGRAFICA', 'SERVICIO', 'TIPOGASTO', 'ESTADO',
                        'MODALIDADLICITACION', 'MODALIDADCONTRATACION','TIPOREAJUSTE',
                        'TIPO_PERFIL', 'MANDANTE')

for i in posibles_categoricos:
    contratos_df[i] = contratos_df[i].astype('category')

contratos_df['FECHAINICIO'] = contratos_df['FECHAINICIO'].apply(lambda x: x[:6] + '20' + x[6:])
contratos_df['FECHATERMINO'] = contratos_df['FECHATERMINO'].apply(lambda x: x[:6] + '20' + x[6:])
contratos_df['FECHATERMINOORIGINAL'] = contratos_df['FECHATERMINOORIGINAL'].apply(lambda x: x[:6] + 
                                                                                  '20' + x[6:])

contratos_df['FECHAINICIO'] = pd.to_datetime(contratos_df['FECHAINICIO'], format="%d/%m/%Y",
                                             errors='coerce')
contratos_df['FECHATERMINO'] = pd.to_datetime(contratos_df['FECHATERMINO'], format="%d/%m/%Y",
                                              errors='coerce')
contratos_df['FECHATERMINOORIGINAL'] = pd.to_datetime(contratos_df['FECHATERMINOORIGINAL'],
                                                      format="%d/%m/%Y", errors='coerce')

# Creacion de pagos_df
pagos_df = pd.read_csv(os.path.join('data', 'pagos.csv'))

posibles_categoricos = ('REGIONGEOGRAFICA', 'SERVICIO', 'SUBTITULO', 'ITEM', 'ASIGNACION')
for i in posibles_categoricos:
    pagos_df[i] = pagos_df[i].astype('category')

pagos_df['FECHA_DOCUMENTO'] = pagos_df['FECHA_DOCUMENTO'].apply(lambda x: x[:6] + '20' + x[6:] if isinstance(x, str) else np.nan)
pagos_df['FECHA_INGRESO_MOP'] = pagos_df['FECHA_INGRESO_MOP'].apply(lambda x: x[:6] + '20' + x[6:] if isinstance(x, str) else np.nan)
pagos_df['FECHAPAGO'] = pagos_df['FECHAPAGO'].apply(lambda x: x[:6] + '20' + x[6:] if isinstance(x, str) else np.nan)

pagos_df['FECHA_DOCUMENTO'] = pd.to_datetime(pagos_df['FECHA_DOCUMENTO'], format="%d/%m/%Y", errors='coerce')
pagos_df['FECHA_INGRESO_MOP'] = pd.to_datetime(pagos_df['FECHA_INGRESO_MOP'], format="%d/%m/%Y", errors='coerce')
pagos_df['FECHAPAGO'] = pd.to_datetime(pagos_df['FECHAPAGO'], format="%d/%m/%Y", errors='coerce')

pagos_df.drop(columns='AGNO')

# Creacion de requisitos_df
requisitos_df = pd.read_csv('data/requisitos.csv')
posibles_categoricos = ('NOMBRE_TIPOREGISTRO', 'CODIGO_ESPECIALIDAD', 'CODIGO_CATEGORIA',
                        'NOMBRE_CATEGORIA')
for i in posibles_categoricos:
    requisitos_df[i] = requisitos_df[i].astype('category')