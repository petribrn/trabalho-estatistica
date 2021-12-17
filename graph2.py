from generateDataframe import df
import matplotlib.pyplot as plt
import seaborn as sns

df_copy = df
df_copy["freq"] = df.groupby('country')["country"].transform("count")

countries = df_copy[["country", "freq", 'avg_vote']].drop_duplicates()

top_countries = countries.nlargest(1607,"freq")
top_countries.reset_index(drop=True, inplace=True)
top_countries.groupby('country')['avg_vote'].agg(['min', 'max'])

plt.figure(figsize=(20,10))
sns.boxplot(data=top_countries, x='country', y='avg_vote')
plt.xticks(rotation=30)
plt.xlabel("País")
plt.ylabel("Nota")
plt.tight_layout()
plt.savefig("./img-graphs/notas_por_pais.png")
plt.tight_layout()


plt.show()