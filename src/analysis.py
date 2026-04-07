import pandas as pd

def state_wise_cases(df):
    return df.groupby('State/UT')['Number of Cases - Registered'].sum()

def year_trend(df):
    return df.groupby('Year')['Number of Cases - Registered'].sum()

def conviction_rate(df):
    df['Conviction Rate'] = (
        df['Number of Police Personel - Convicted'] /
        df['Number of Police Personel - Arrested']
    ).fillna(0)

    return df[['State/UT', 'Conviction Rate']]

def top_states(df):
    return df.groupby('State/UT')['Number of Cases - Registered'].sum().nlargest(5)