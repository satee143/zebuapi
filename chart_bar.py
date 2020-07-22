import os

import plotly.graph_objects as go

import pandas as pd


def create_chart(df):
    df = df.head(30)
    fig = go.Figure(data=[go.Ohlc(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
    fig.show()


os.chdir('/storage/emulated/0/bluetooth')
if __name__ == '__main__':
    create_chart(pd.read_excel('c.xlsx'))
