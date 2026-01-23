import matplotlib
matplotlib.use('Agg')

import yfinance as yf
import mplfinance as mpf
import datetime

import plotly
import plotly.io as pio


# makes .png graphs using matplotlib-finance
def getStaticGraphs(tickers, period, interval, type, mav):

    for ticker in tickers:
        history = yf.download(tickers=ticker, period=period, interval=interval, multi_level_index=False)
        mpf.plot(history, style='yahoo', type=type, mav=mav, title=ticker + ' ' + datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"), tight_layout=True, figratio=(10, 5), savefig='static/' + ticker)


# makes interactive graphs using plotly
def getInteractiveGraphs(tickers, period, interval, chart_type, yaxis_title):
    graphs = []
    for symbol, full_name in tickers.items():
        # get data from yahoo finance
        data = yf.download(tickers=symbol, period=period, interval=interval, multi_level_index=False)
        # create plotly graph
        if chart_type == 'Candlestick':
            fig = plotly.graph_objects.Figure(data=[plotly.graph_objects.Candlestick(x=data.index,
                                        open=data['Open'],
                                        high=data['High'],
                                        low=data['Low'],
                                        close=data['Close'])])

        elif chart_type == 'Line':
            fig = plotly.graph_objects.Figure(data=[plotly.graph_objects.Scatter(
                                        x=data.index,
                                        y=data['Close'],
                                        mode='lines')])

        #MakeItLookPretty.exe
        fig.update_layout(height=500, width=900, margin=dict(t=80,b=40,l=40,r=40), 
                            title={'text':full_name, 'font':{'family':"Verdana", 'size':18, 'weight':1000}}, yaxis_title=yaxis_title)
        #convert to HTML (don't have to save image), full_html=False returns only the div
        graphs.append(pio.to_html(fig, full_html=False))

    return graphs