import requests
import pandas as pd
from io import StringIO
import pickle


file_path = "ticker_to_cik.txt"

# Read the file into a DataFrame
df = pd.read_csv(file_path, sep='\t', header=None, names=["Symbol", "CIK"])


df['CIK'] = df['CIK'].apply(lambda x: str(x).zfill(10))


df.set_index('Symbol', inplace=True)


output_file_path = 'ticker_to_cik_processed.csv'
df.to_csv(output_file_path)

print(f"DataFrame saved to {output_file_path}")



with open('CIK_mapping.pkl', 'wb') as file:
    pickle.dump(df, file)

