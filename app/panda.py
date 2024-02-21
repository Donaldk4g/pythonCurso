import pandas as pd

df=pd.read_csv('data.csv')
df = df[df['Continent']=='Africa'] #filtrar datos por una columna y datos que contenga esa columna


countries= df['Country/Territory'].values
porcentajes=df['World Population Percentage'].values
print(df)