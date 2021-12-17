import pandas as pd

# Apenas para reduzir o numero de linhas no print
pd.set_option("display.max_rows", 30000)
pd.set_option("display.max_columns", 5)

# Ler o conjunto de dados
raw_df = pd.read_csv("./data/IMDb_movies.csv", low_memory=False)

#Remove colunas indesejadas
colsToDrop = ["imdb_title_id","original_title","date_published","duration",
              "language","director","writer","production_company","actors","description",
              "budget","usa_gross_income","worlwide_gross_income","metascore",
              "votes","reviews_from_users","reviews_from_critics"]

# Dataframe contendo titulo, ano, genero, pais e nota
main_df = raw_df.drop(colsToDrop, axis=1)

# Tratamento do dataframe
main_df = main_df.drop(index=83917)
main_df["country"] = main_df["country"].astype(str)
main_df["year"] = pd.to_numeric(main_df["year"])
main_df["avg_vote"] = pd.to_numeric(main_df["avg_vote"])

df = main_df[~main_df["country"].str.contains(",")].reset_index(drop=True)
df = df[~df["genre"].str.contains(",")].reset_index(drop=True)
# Usar o 'df' para geracao de graficos

# Export do dataframe.csv para usar no data studio
compression_opts = dict(method='zip', archive_name='dataframe.csv')
df.to_csv('./data/dataframe.zip', index=False, compression=compression_opts)








