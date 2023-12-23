# Fichero librería donde se encuentran todas las funciones llamadas desde main.py
import krakenex
from pykrakenapi import KrakenAPI
import streamlit
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# data_load(): carga de datos
def data_load():

    # carga de API 
    api = krakenex.API()
    k = KrakenAPI(api)

    # seleccion del par 
    pair = input('Seleccion de par de criptos: ')

    # get_ohlc_data() de Kraken para obtener los datos
    if pair == "ETHUSD":
        data = k.get_ohlc_data("ETHUSD", interval = 1440, ascending = True)
    elif pair == "USDTUSD":
        data = k.get_ohlc_data("USDTUSD", interval = 1440, ascending = True)    
    elif pair == "BTCUSD":
        data = k.get_ohlc_data("BTCUSD", interval = 1440, ascending = True)    
    elif pair == "XRPUSD":
        data = k.get_ohlc_data("XRPUSD", interval = 1440, ascending = True)    
    elif pair == "SOLUSD":
        data = k.get_ohlc_data("SOLUSD", interval = 1440, ascending = True) 
    else: 
        print('No se ha seleccionado ninguna moneda')

    # conversión de los datos a DataFrame
    df= pd.DataFrame(data[0])

    return(df)

# data_clean(): limpieza de datos
def data_clean(df): 
    df_clean = df.copy()
    df_clean.drop('vwap', axis=1, inplace=True)

    if df_clean.isnull().sum().sum() != 0:
        print(df_clean.isnull().sum())
        df_clean = df_clean.ffill() # toma el valor anterior de la columna

    return(df_clean)

# data_close(): dataFrame con con precios de cierre
def data_close(df_clean):
    df_close = pd.DataFrame()
    df_close=df_clean.close

    return(df_close)
    


# candlegraf(): función para gráfico de velas
def candle_graph(df_clean):
    # gráfica
    fig = go.Figure(data = [go.Candlestick(x=df_clean.index,
                                         open=df_clean['open'],
                                         high=df_clean['high'],
                                         low=df_clean['low'],
                                         close=df_clean['close'])])
    fig.show()     


def line_graph(df_close):
    # variables de tiempo
    df_close['Month'] = df_close.index.month
    df_close = df_close.assign(Month_str = df_close.Month.map({1:"Enero", 2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre",12:"Diciembre"}))
    df_close['Year'] = df_close.index.year
    df_close['Month_year'] = df_close['Month_str'] + " " + df_close['Year'].astype(str)

    # grafico de index-close
    plt.plot(df_close.index, df_close[0])

    # configurar grafico

# estochastic(): grafica del estocastico en el tiempo
def estochastic_graph(df_clean):
    # indicadores estocásticos 
    # calculo de estoscastico => estocastico =  (close - low)/(high-low)
    df_clean["Estocastico"] = 100*(df_clean["close"]- df_clean["low"])/(df_clean["high"]-df_clean["low"])
    plt.plot(df_clean.index, df_clean["Estocastico"])

# grafico de media movil del precio de cierre
def avg_graph(df_clean):
    period = 30
    df_clean['media_movil'] = df_clean['close'].rolling(window=period).mean()
    plt.plot(df_clean.index, df_clean["media_movil"])

# grafico conjunto de media movil y estocastico
def mixed_graph(df_clean):
    plt.plot(df_clean.index, df_clean["Estocastico"])
    plt.plot(df_clean.index, df_clean["media_movil"])


df = data_load()
df_clean = data_clean(df)
df_close = data_close(df_clean)
candle_graph(df_clean)
line_graph(df_close)
estochastic_graph(df_clean)
avg_graph(df_clean)
mixed_graph(df_clean)