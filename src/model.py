from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    df = df.fillna(0)

    df['target'] = df['Number of Police Personel - Convicted'] > 0

    X = df[['Number of Cases - Registered',
            'Number of Police Personel - Arrested']]

    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, accuracy