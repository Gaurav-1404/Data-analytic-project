import pandas as pd

df1 = pd.read_csv("2016 Cases against Police Personnels.csv")
df2 = pd.read_csv("2017 Cases against Police Personnels.csv")
df3 = pd.read_csv("2018 Cases against Police Personnels.csv")

df1['Year'] = 2016
df2['Year'] = 2017
df3['Year'] = 2018

df = pd.concat([df1, df2, df3])
df.to_csv("crime_data.csv", index=False)

print("Done ✅")