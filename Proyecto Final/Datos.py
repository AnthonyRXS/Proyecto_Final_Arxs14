import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('Carbon_Dioxide_Emission_Estimates.csv')


# Filtrar los datos según la columna 'Type'
df_emisions_co2 = df[df['Type'] == 'Emissions (thousand metric tons of carbon dioxide)']
df_emisions_co2_per_capita = df[df['Type'] == 'Emissions per capita (metric tons of carbon dioxide)']

# Mostrar los primeros registros de cada DataFrame
print(df_emisions_co2.head())
print(df_emisions_co2_per_capita.head())