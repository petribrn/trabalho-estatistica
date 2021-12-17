from generateDataframe import df
import matplotlib.pyplot as plt

df_copy = df
df_copy["freq"] = df.groupby('year')["year"].transform("count")

countries = df_copy[["year", "freq"]].drop_duplicates()

years = countries.nlargest(110,"freq")
years.reset_index(drop=True, inplace=True)

plt.figure(figsize=(20,10))
plt.hist(years['year'],years["freq"], width=1)
plt.xticks(rotation=30)
plt.title("Número de filmes por ano")
plt.xlabel("Ano")
plt.ylabel("Nº de filmes")
plt.tight_layout()
plt.savefig('./img-graphs/num_filmes_ano.png')
plt.show()
