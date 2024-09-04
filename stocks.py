import pandas as pd
import numpy as np

stocks = pd.read_csv('cleaned_data.csv')


import pandas as pd

# Load the stocks data
stocks = pd.read_csv('cleaned_data.csv')

# Create the first DataFrame with 'Symbol' and 'momentum' columns
df1 = pd.DataFrame()
df1['Symbol'] = stocks['Symbol']
df1['ROE'] = stocks['ROE']
df1['SE'] = stocks['SE']
df1['Net Income'] = stocks['Net Income']
df1['momentum'] = 0  # Initialize momentum with a default value (e.g., 0)
date_columns = stocks.loc[:, '2022-01-03':'2022-12-30']
# Calculate the standard deviation across the selected date columns for each row (stock)
df1['annualized daily std'] = date_columns.std(axis=1) * np.sqrt(252)

# Display the updated DataFrame
# Calculate momentum as (price on '2023-06-01' - price on '2023-01-04') / price on '2023-06-01'
df1['momentum'] = (stocks['2023-06-01'] - stocks['2023-01-04']) / stocks['2023-01-04']

df1['factor'] = df1['momentum'] / df1['annualized daily std']

df1.to_csv('2023_period1.csv', index=False)


# # Create the second DataFrame with 'Symbol' and 'momentum' columns
df2 = pd.DataFrame()
df2['Symbol'] = stocks['Symbol']
df2['ROE'] = stocks['ROE']
df2['SE'] = stocks['SE']
df2['Net Income'] = stocks['Net Income']
df2['momentum'] = 0  # Initialize momentum with a default value (e.g., 0)
df2['momentum'] = (stocks['2023-12-29'] - stocks['2023-06-02']) / stocks['2023-06-02']
date_columns = stocks.loc[:, '2022-06-01':'2023-06-01']
# Calculate the standard deviation across the selected date columns for each row (stock)
df2['annualized daily std'] = date_columns.std(axis=1) * np.sqrt(252)
df2['factor'] = df2['momentum'] / df2['annualized daily std']
df2.to_csv('2023_period2.csv', index=False)

# Now df1 and df2 bo
