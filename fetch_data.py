import subprocess, json

class Data():  
    def __init__(self, stock):  
        self.stock = stock
    '''
    get_fundamentals - get fundamental data for a particular security
    Params:
    Returns:
        An array of dictionary entries containing:
        { 
            "open": <Price in US Dollars>,
            "high": <Highest price in US Dollars>,
            "low": <Lowest price in US Dollars>,
            "volume": <Volume>,
            "average_volume": <Average volume>,
            "high_52_weeks": <Highest price over 52 weeks in US Dollars>,
            "low_52_weeks": <Lowest price over 52 weeks in US Dollars>,
            "market_cap": <Market cap in US Dollars>,
            "dividend_yield": <Dividend yield in US Dollars>,
            "pe_ratio": <PE ratio>,
            "description": <Description of security>,
            "instrument": <URL back to security's instrument data>
        }
    '''
    def get_fundamentals(self):
        fundamental_command = f'curl -v https://api.robinhood.com/fundamentals/{self.stock}/ -H "Accept: application/json"'
        p = subprocess.Popen(fundamental_command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
        out, err = p.communicate()
        parsed = json.loads(out)
        return parsed

    '''
    get_quote - get quote data for a particular security
    Params:
    Returns:
        An array of dictionary entries containing:
        { 
            "ask_price": <Price in US Dollars>,
            "ask_size": <size>,
            "bid_price": <Price in US Dollars>,
            "bid_size": <Price in US Dollarys>,
            "last_trade_price": <Price in US Dollarys>,
            "last_extended_hours_trade_price": <Price in US Dollarys>,
            "previous_close": <Price in US Dollarys>,
            "adjusted_previous_close": <Price in US Dollarys>,
            "previous_close_date": <Date>,
            "symbol": <Symbol>,
            "trading_halted": <Boolean>,
            "updated_at": <Last update UTC time>
        }
    '''
    def get_quote(self):
        quote_command = f'curl -v https://api.robinhood.com/quotes/historicals/{self.stock}/'
        p = subprocess.Popen(quote_command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
        out, err = p.communicate()
        parsed = json.loads(out)
        return parsed

    '''
    get_quote_historicals - get historical data for a particular security
    Params:
        - interval=week|day|10minute|5minute|null(all) 
        - span=day|week|year|5year|all
        - bounds=extended|regular|trading
    Returns:
        An array of dictionary entries containing relevant data:
        {
            "begins_at": <time in UTC>,
            "close_price": <Price in US Dollars>,
            "high_price": <Price in US Dollars>,
            "interpolated": <Boolean>,
            "low_price": <Price in US Dollars>,
            "open_price": <Price in US Dollars>,
            "session":
            "reg",
            "volume": <Volume traded>
        }
    '''
    def get_quote_historicals(self, interval='day', span='year', bounds='extended'):
        quote_command = f'curl -v https://api.robinhood.com/quotes/historicals/{self.stock}/?interval={interval}&span={span}&bounds={bounds}'
        p = subprocess.Popen(quote_command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
        out, err = p.communicate()
        parsed = json.loads(out)
        return parsed['historicals']

    '''
    get_news - get news about a particular security for past month
    Params:
    Returns:
        An array of dictionary entries containing:
        {
            "api_source": <API source>,
            "author": <author>,
            "instrument": <instrument>,
            "num_clicks": <number of clicks on news item>,
            "preview_image_url": <url>,
            "preview_image_width": <width>,
            "preview_image_height": <height>,
            "published_at": <ISO891 date>,
            "relay_url": <url>,
            "source": <source name>,
            "summary": <short description>,
            "title": <title of news item>,
            "updated_at": <ISO891 date>,
            "uuid": <RobinHood id>,
            "currency_id": <currency id>
        }
    '''
    def get_news():
        news = []
        news_command = f'curl -v https://api.robinhood.com/midlands/news/{self.stock}/'
        p = subprocess.Popen(news_command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
        out, err = p.communicate()
        parsed = json.loads(out)
        news += parsed['results']
        page = 1
        valid_page = True
        while valid_page:
            news_command = f'curl -v https://api.robinhood.com/midlands/news/{stock}/?page={page}'
            p = subprocess.Popen(news_command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)  
            out, err = p.communicate()
            parsed = json.loads(out)
            if 'results' in parsed:
                news += parsed['results']
                page+=1
            else:
                valid_page = False
        return news
