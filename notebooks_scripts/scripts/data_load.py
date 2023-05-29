import pandas as pd

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
    df['Total_Acidity'] = df['fixed_acidity'] + df['volatile_acidity']
    #Fixed Acidity Ratio
    df['Fixed_Acidity_Ratio'] = df['fixed_acidity'] / df['Total_Acidity']
    #Sugar to Acidity Ratio
    df['Sugar_Acidity_Ratio'] = df['residual_sugar'] / df['Total_Acidity']
    #Free-Sulphure_Dioxide / Total Sulphure Diocxide
    df['FreeSulphure_Ratio'] = df['free_sulfur_dioxide'] / df['total_sulfur_dioxide']
    #Alcohol x  pH
    df['Alcohol_x_pH'] = df['alcohol'] * df['pH']
    return df