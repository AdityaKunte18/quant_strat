import pandas as pd


stocks = pd.read_csv('cleaned_data.csv')


import pandas as pd

# Load the stocks data
stocks = pd.read_csv('cleaned_data.csv')

# Create the first DataFrame with 'Symbol' and 'momentum' columns
df1 = pd.DataFrame()
df1['Symbol'] = stocks['Symbol']
df1['momentum'] = 0  # Initialize momentum with a default value (e.g., 0)

# Calculate momentum as (price on '2023-06-01' - price on '2023-01-04') / price on '2023-06-01'
df1['momentum'] = (stocks['2023-06-01'] - stocks['2023-01-04']) / stocks['2023-06-01']

df1.to_csv('2023_period1.csv', index=False)


# # Create the second DataFrame with 'Symbol' and 'momentum' columns
df2 = pd.DataFrame()
df2['Symbol'] = stocks['Symbol']
df2['momentum'] = 0  # Initialize momentum with a default value (e.g., 0)
df2['momentum'] = (stocks['2023-12-29'] - stocks['2023-06-02']) /stocks['2023-12-29']

df2.to_csv('2023_period2.csv', index=False)

# Now df1 and df2 bo
