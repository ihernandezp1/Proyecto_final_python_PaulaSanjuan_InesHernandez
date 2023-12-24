import pandas as pd
import krakenex
from pykrakenapi import KrakenAPI
import plotly.graph_objects as go


class Data: 
    def __init__(self): 
        self.api = krakenex.API()
        self.data = None  # DataFrame con los datos descargados
        self.data_close = None  # DataFrame con los precios de cierre
        self.pair_type = None  # Tipo de par representado

    def set_pair_type(self, pair): 
        pair1 = pair.split('/')[0]
        pair2 = pair.split('/')[1]
        self.pair_type =  pair1+pair2# Ejemplo: 'XBT/USD' -> 'USD'

    def get_data(self,pair): 
        try: 
            k = KrakenAPI(self.api)
            ohlc_result = k.get_ohlc_data(self.pair_type, interval = 1440, ascending = True)
            if ohlc_result==None:
                raise Exception(f"Error en la solicitud OHLC: {ohlc_result['error']}")
            
            self.data = pd.DataFrame(ohlc_result[0])
            self.data_close = self.data['close']
        except Exception as e:
            print(f"Error al obtener datos OHLC: {e}")
    
    # def get_pairs(self): 
    #     pairs = self.pair_type
    #     return pairs
    
    def data_clean(self): 
        self.data.drop('vwap', axis=1, inplace=True)
        self.data.drop('count', axis=1, inplace=True)
        if self.data.isnull().sum().sum() != 0:
            print(self.data.isnull().sum())
            self.data.ffill() # toma el valor anterior de la columna
        return self.data
            
    def candle_graph(self):
        # gráfica
        fig = go.Figure(data = [go.Candlestick(x=self.data.index,
                                            open=self.data['open'],
                                            high=self.data['high'],
                                            low=self.data['low'],
                                            close=self.data['close'])])
        # fig.show()
        return fig     