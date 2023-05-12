import pandas as pd

def data_reading():
    train_df = pd.read_csv('../../data/train.csv')
    test_df = pd.read_csv('../../data/test.csv')
    return train_df, test_df