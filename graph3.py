from generateDataframe import df
import matplotlib.pyplot as plt
import seaborn as sns

df_copy = df
df_copy["freq"] = df.groupby('genre')["genre"].transform("count")

genres = df_copy[["genre", "freq", "avg_vote"]].drop_duplicates()
genres = genres.sort_values(by=['freq'], ascending=False)
genres.groupby('genre')['avg_vote'].agg(['min', 'max'])

top_genres = genres.nlargest(996,"freq")
top_genres.reset_index(drop=True, inplace=True)

plt.figure(figsize=(20,10))
sns.boxplot(data=top_genres, x='genre', y='avg_vote')
plt.xticks(rotation=45, fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel("Gênero", fontsize=20)
plt.ylabel("Nota", fontsize=20)
plt.tight_layout()
plt.savefig("./img-graphs/notas_por_genero.png")
plt.show()