import pickle
import yfinance as yf

# Load the existing DataFrame from a pickle file
with open('daily_data_2023.pkl', 'rb') as file:
    daily_data = pickle.load(file)

# Initialize the list for unrecognized symbols
unrecognized_symbols = []

# Iterate over each ticker symbol in the DataFrame index
for ticker in daily_data.index:
    if ticker == 'SW':
        continue
    try:
        # Download the stock data for the given ticker and date range
        stock_data = yf.download(ticker, start='2023-01-01', end='2023-12-31')
        
        # Check if the stock data is empty, indicating an unrecognized symbol
        if stock_data.empty:
            print(f"Symbol not recognized: {ticker}")
            unrecognized_symbols.append(ticker)
            continue
        
        # Check if the 'Adj Close' column is present in the stock data
        if 'Adj Close' in stock_data.columns:
            # Find the intersection of dates between stock data and DataFrame columns
            valid_dates = stock_data.index.intersection(daily_data.columns)
            
            # Update the DataFrame with the adjusted close prices for the valid dates
            daily_data.loc[ticker, valid_dates] = stock_data.loc[valid_dates, 'Adj Close']
    
    except Exception as e:
        # Handle any errors during the data fetching process
        print(f"Error fetching data for {ticker}: {e}")
        unrecognized_symbols.append(ticker)

# Print the list of unrecognized symbols
print("Unrecognized symbols:", unrecognized_symbols)

# Save the list of unrecognized symbols to a text file
with open('unrecognized_symbols.txt', 'w') as file:
    for symbol in unrecognized_symbols:
        file.write(f"{symbol}\n")

# Save the updated DataFrame to a pickle file
with open('daily_data_2023_updated.pkl', 'wb') as file:
    pickle.dump(daily_data, file)
