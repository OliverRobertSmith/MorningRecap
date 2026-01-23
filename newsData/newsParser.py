import feedparser


# getting news data from rss URLs using feedparser
def getNews(tickers, totalArticles):
    newsInfo=[]
    for symbol, _ in tickers.items():

        rss_url = f'https://feeds.finance.yahoo.com/rss/2.0/headline?s={symbol}&region=US&lang=en-US%22'

        feed = feedparser.parse(rss_url)

        # get entries relating to the ticker
        for entry in feed.entries[:totalArticles]:
            newsInfo.append(entry)
    
    #chunk the return into groups
    newsInfo = list(chunked(newsInfo, totalArticles))
    return newsInfo


def chunked(list, n):
    for i in range(0, len(list), n):
        yield list[i:i+n]
