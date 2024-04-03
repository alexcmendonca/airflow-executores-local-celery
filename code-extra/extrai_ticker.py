import yfinance

def extrai_dados(ticker, start_date, end_date):
    caminho = f"/home/alexmend/Documents/airflowalex/code-extra/acoes/{ticker}.csv"
    yfinance.Ticker(ticker).history(
        period = "1d",
        interval = "1h",
        start = start_date,
        end = end_date,
        prepost = True
    ).to_csv(caminho)


extrai_dados("AAPL", "2024-02-19", "2024-02-23")
extrai_dados("GOOG", "2024-03-18", "2024-03-22")