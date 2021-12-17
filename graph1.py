from generateDataframe import df
import matplotlib.pyplot as plt

df_copy = df
df_copy["freq"] = df.groupby('country')["country"].transform("count")
countries = df_copy[["country", "freq"]].drop_duplicates()

top_countries = countries.nlargest(30,"freq")
top_countries.reset_index(drop=True, inplace=True)

plt.figure(figsize=(20,10))
plt.bar(top_countries["country"],top_countries["freq"], width=0.8)
plt.xticks(rotation=90)
plt.xlabel("País")
plt.ylabel("Nº de filmes")
plt.tight_layout()

plt.savefig("./img-graphs/num_filmes_pais.png")
plt.show()

