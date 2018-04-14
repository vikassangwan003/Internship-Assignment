import pandas as pd

df=pd.read_json("imdb.json")
#print(df)
df.to_csv('results.csv')
df1=pd.read_csv('results.csv')
#print(df1.head())
df2=df1[df1['genre'].str.contains('Action') ]
#df3=df2.sort_values('imdb_score',ascending=False)
#print(df3.iloc[:3,[2,4,5]])
print(df2.loc[df2.sort_values('imdb_score',ascending=False).index,['name','director']].head(3))
