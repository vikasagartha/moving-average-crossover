import pandas as pd
import numpy as np
from fetch_data import Data
import matplotlib.pyplot as plt

close_key = 'close'
date_key = 'date'
fast_key = 'fast'
slow_key = 'slow'

def main(sym, fast_rate = 20, slow_rate = 50, tolerance = 0.01, show_plot = False):
    if(sym is None):
        print('Err: no symbol provided')
        return

    data = Data(sym)
    quote_data = data.get_quote_historicals(interval='day', span='day', bounds='extended')

    if(len(quote_data) == 0):
        print('Err: no data for symbol {0}'.format(sym))
        return

    df = pd.DataFrame(quote_data)
    df['close_price'] = df['close_price'].astype(float)
    df = df.rename(index=str, columns={'begins_at': date_key, 'close_price': close_key})

    df[date_key]  = pd.to_datetime(df[date_key])
    df = df.set_index(date_key)

    df[slow_key] = df[close_key].rolling(slow_rate).mean()
    df[fast_key] = df[close_key].rolling(fast_rate).mean()

    prev = df.iloc[-2]
    last = df.iloc[-1]

    close_tolerance = last.at[close_key]*tolerance
    last_absolute_diff = abs(last.at[fast_key] - last.at[slow_key])

    fast_is_increasing = (last.at[fast_key] - prev.at[fast_key]) > 0

    if(last_absolute_diff < close_tolerance and fast_is_increasing):
        print(sym+': enter')
    elif(last_absolute_diff < close_tolerance and not(fast_is_increasing)):
        print(sym+': exit')
    else:
        print(sym+': hold')

    if(show_plot):
        df[close_key].plot(grid=True,figsize=(8,5))
        df[slow_key].plot(grid=True,figsize=(8,5))
        df[fast_key].plot(grid=True,figsize=(8,5))
        plt.show(block=True)
