import pickle
import yfinance as yf

with open('daily_data_2023.pkl', 'rb') as file:
    daily_data = pickle.load(file)


unrecognized_symbols = []


for ticker in daily_data.index:
    try:
       
        stock_data = yf.download(ticker, start='2023-01-01', end='2023-12-31')
        
        
        if stock_data.empty:
            print(f"Symbol not recognized: {ticker}")
            unrecognized_symbols.append(ticker)
            continue
        
      
        if 'Adj Close' in stock_data.columns:
         
            valid_dates = stock_data.index.intersection(daily_data.columns)
            
         
            daily_data.loc[ticker, valid_dates] = stock_data.loc[valid_dates, 'Adj Close']
    
    except Exception as e:
        
        print(f"Error fetching data for {ticker}: {e}")
        unrecognized_symbols.append(ticker)


print("Unrecognized symbols:", unrecognized_symbols)


with open('unrecognized_symbols.txt', 'w') as file:
    for symbol in unrecognized_symbols:
        file.write(f"{symbol}\n")


daily_data.to_csv('daily_stock_prices.csv')