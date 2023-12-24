
import plotly.graph_objects as go

class Indicators: 
    def __init__(self):
        self.dfdata = None

    def set_indicators(self, data):
        self.dfdata = data

    def line_graph(self):
        # # variables de tiempo
        # df_close['Month'] = df_close.index.month
        # df_close = df_close.assign(Month_str = df_close.Month.map({1:"Enero", 2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre",12:"Diciembre"}))
        # df_close['Year'] = df_close.index.year
        # df_close['Month_year'] = df_close['Month_str'] + " " + df_close['Year'].astype(str)

        # grafico de index-close
        # fig = plt.plot(self.dfdata.index, self.dfdata["close"])
        # return fig
        # configurar grafico

        fig = go.Figure()
        fig.add_trace(go.Scatter(x = self.dfdata.index, y = self.dfdata["close"], mode='lines'))
        return fig

    # estochastic(): grafica del estocastico en el tiempo
    def stochastic_graph(self):
        # indicadores estocásticos 
        # calculo de estoscastico => estocastico =  (close - low)/(high-low)
        self.dfdata["Estocastico"] = 100*(self.dfdata["close"]- self.dfdata["low"])/(self.dfdata["high"]-self.dfdata["low"])
        #fig = plt.plot(self.dfdata.index, self.dfdata["Estocastico"])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = self.dfdata.index, y = self.dfdata["Estocastico"], mode='lines'))
        return fig

    # grafico de media movil del precio de cierre
    def avg_graph(self):
        period = 30
        self.dfdata['media_movil'] = self.dfdata['Estocastico'].rolling(window=period).mean()
        self.dfdata['media_movil_close'] = self.dfdata['close'].rolling(window=period).mean()
        #plt.plot(self.data.index, self.data["media_movil"])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = self.dfdata.index, y = self.dfdata["media_movil"], mode='lines'))



        return fig

    # grafico conjunto de media movil y estocastico
    def mixed_graph(self):
        # plt.plot(self.data.index, self.data["close"])
        # plt.plot(self.data.index, self.data["media_movil"])
        # plt.plot(self.data.index, self.data["Estocastico"])
        fig = go.Figure()
        # fig.add_trace(go.Scatter(x = self.dfdata.index, y = self.dfdata["close"], mode='lines', name= 'Precio de cierre'))
        fig.add_trace(go.Scatter(x = self.dfdata.index, y = self.dfdata["Estocastico"], mode='lines', name = 'Estocástico', line=dict(color='#0077cc')))
        fig.add_trace(go.Scatter(x = self.dfdata.index, y = self.dfdata["media_movil"], mode='lines', name = 'Media móvil', line=dict(color='red', width=2)))

        return fig
    
    # grafico conjunto de media movil y precios de cierre
    def avg_close(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = self.dfdata.index, y = self.dfdata["close"], mode='lines', name= 'Precio de cierre',line=dict(color='#0077cc')))
        fig.add_trace(go.Scatter(x = self.dfdata.index, y = self.dfdata["media_movil_close"], mode='lines', name = 'Media móvil',line=dict(color='red', width=2)))

        return fig

