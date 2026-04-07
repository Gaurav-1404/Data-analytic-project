import pandas as pd

def load_data():
    df = pd.read_csv("data/crime_data.csv")
    return df

def clean_data(df):
    df = df.fillna(0)

    # Remove unwanted column
    if 'S. No.' in df.columns:
        df = df.drop(columns=['S. No.'])

    df['Year'] = df['Year'].astype(int)

    return df