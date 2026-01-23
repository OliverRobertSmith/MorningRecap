from flask import Flask, render_template, url_for
from stockData import stock_graphs
from newsData import newsParser

country_index_tickers = {'^SPX':'USA - S&P 500', '^FTSE':'UK - FTSE 100', '^FCHI':'FRANCE - CAC 40', '^GDAXI':'GERMANY - DAX', '^N225':'CHINA - NIKKEI 225'}
individual_stock_tickers = {'NVDA':'NVIDIA', 'TSLA':'TESLA', 'MSFT':'MICROSOFT', 'AAPL':'APPLE'}
totalArticles = 10

app = Flask(__name__)

if __name__ == 'main':
    app.run(debug=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/worldbenchmarks')
def worldbenchmarks():
    figures = stock_graphs.getInteractiveGraphs(country_index_tickers, period='30y', interval='1mo', chart_type='Line', yaxis_title='Points')
    news = newsParser.getNews(country_index_tickers, totalArticles)
    pairs = zip(figures, news)     # zip together so all data corresponds to the same company
    return render_template('worldbenchmarks.html', pairs=pairs)

@app.route('/individualStocks')
def individualStocks():
    figures = stock_graphs.getInteractiveGraphs(individual_stock_tickers, period='1y', interval='1d', chart_type='Candlestick', yaxis_title='Price ($)')
    news = newsParser.getNews(individual_stock_tickers, totalArticles)
    pairs = zip(figures, news)     # zip together so all data corresponds to the same company
    return render_template('individualStocks.html', pairs=pairs)