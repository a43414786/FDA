import pandas as pd

import pandas as pd
import numpy as np
def preprocess(df:pd.DataFrame):

    df.replace(to_replace=np.nan, value=0, inplace=True)
    
    df['abnormal_Ndir'] = 0
    df['abnormal_Ndir'][(df['Ndir'] < -720) | (df['Ndir'] > 720)] = 1
    # df['abnormal_Ndir'].unique()

    df[(df['Wdir'] < -180) | (df['Wdir'] > 180)]

    df['abnormal_Wdir'] = 0
    df['abnormal_Wdir'][(df['Wdir'] < -180) | (df['Wdir'] > 180)] = 1
    # df['abnormal_Wdir'].unique()

    df[(df['Patv'] <= 0) & (df['Wspd'] > 2.5)]

    df['unknown_Patv'] = 0
    df['unknown_Patv'][(df['Patv'] <= 0) & (df['Wspd'] > 2.5)] = 1
    # df['unknown_Patv'].unique()

    df[(df['Pab1'] > 89) & (df['Pab2'] > 89) & (df['Pab3'] > 89)]

    df['unknown_Pab'] = 0
    df['unknown_Pab'][(df['Pab1'] > 89) & (df['Pab2'] > 89) & (df['Pab3'] > 89)] = 1
    # df['unknown_Pab'].unique()

    df[df['Prtv'] < 0]

    df['Prtv'][df['Prtv'] < 0] = 0

    df['Wdir'][df['Wdir'].notna()] = df['Wdir'][df['Wdir'].notna()].apply(lambda x: int(x) % 360)

    df['Wdir'][(df['Wdir'].notna()) & (df['Wdir'] < -180)] = df['Wdir'][(df['Wdir'].notna()) & (df['Wdir'] < -180)] + 360

    # df['Wdir'].unique()

    df['Ndir'][df['Ndir'].notna()] = df['Ndir'][df['Ndir'].notna()].apply(lambda x: int(x) % 360)

    df['Ndir'][(df['Ndir'].notna()) & (df['Ndir'] < -180)] = df['Ndir'][(df['Ndir'].notna()) & (df['Ndir'] < -180)] + 360

    # df['Ndir'].unique()

    return df

