import pickle

with open('daily_data_2023.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print("DataFrame has been loaded successfully.")
print(loaded_data.loc[:, loaded_data.columns.month == 2])  # Display the first few rows to verify
