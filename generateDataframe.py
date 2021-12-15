import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apenas para reduzir o numero de linhas no print
pd.set_option("display.max_rows", 30)
pd.set_option("display.max_columns", 5)

# Ler o conjunto de dados
df = pd.read_csv("./IMDb_movies.csv", low_memory=False)

#Remove colunas indesejadas
colsToDrop = ["imdb_title_id","original_title","date_published","duration",
              "language","director","writer","production_company","actors","description",
              "budget","usa_gross_income","worlwide_gross_income","metascore",
              "votes","reviews_from_users","reviews_from_critics"]

# Dataframe contendo titulo, ano, genero, pais e nota
main_df = df.drop(colsToDrop, axis=1)

main_df = main_df.drop(index=83917)
main_df["year"] = pd.to_numeric(main_df["year"])
main_df["avg_vote"] = pd.to_numeric(main_df["avg_vote"])

"""
    A partir disso, será possível manipular o conjunto de dados para geração de gráficos diversos, 
    apenas por selecionar os eixos por colunas do dataframe.
    
    Exemplo:  plot = sns.boxplot(data=main_df, x="country", y="avg_vote")
    
"""







