import pandas as pd
import numpy as np

def data_reading():
    train_df = pd.read_csv('../../data/train.csv')
    test_df = pd.read_csv('../../data/test.csv')
    train_df.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)
    test_df.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)
    train_df.drop(['Id'], axis=1, inplace= True)
    test_df.drop(['Id'], axis=1, inplace= True)
    return train_df, test_df

def feature_generation(df):
    
    #Total Acidity
    df['total_acidity'] = df['fixed_acidity'] + df['volatile_acidity'] + df['citric_acid']
    
    columns = list(df.columns)

    for i in range(len(columns)):
        for j in range(i+1, len(columns)):
            if columns[i] != 'quality' and columns[j] != 'quality':
                col_name1 = columns[i] + '_' + columns[j] + '_r'
                col_name2 = columns[i] + '_' + columns[j] + '_m'
                df[col_name1] = df[columns[i]] / df[columns[j]]
                df[col_name2] = df[columns[i]] * df[columns[j]]
                df[col_name1] = df[col_name1].replace([np.inf, -np.inf], np.nan)
    
    # MolecularSO2
    df['molecularso2'] = df['free_sulfur_dioxide']/(1+ 10**(df['pH'] -1.81))

    df['alcohol_density_r_totalacidity_r'] = (1 / df['density_alcohol_r']) / df['total_acidity']
    df['total_acidity_sulphates_p'] = df['total_acidity'] + df['sulphates']
    df['density_alcohol_r_sulphates_chlorides_r'] = df['density_alcohol_r'] * 1/df['chlorides_sulphates_r']
    df['total_acidity_alcohol_r+sulphates*alcohol+total_acidity'] = (1 / df['alcohol_total_acidity_r']) + df['sulphates_alcohol_m'] + df['total_acidity']
    
    return df