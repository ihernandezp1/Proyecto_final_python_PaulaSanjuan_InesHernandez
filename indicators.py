
import plotly.graph_objects as go

class Indicators: 
    def __init__(self):
        self.dfdata = None

    def set_indicators(self, data):
        self.dfdata = data

    def line_graph(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = self.dfdata.index, 
                                 y = self.dfdata["close"], mode='lines'))
        return fig

    # estochastic(): grafica del estocastico en el tiempo
    def stochastic_graph(self):
        # indicadores estocásticos 
        # cálculo de estocástico => estocástico =  (close - low)/(high-low)
        close = self.dfdata["close"]
        low = self.dfdata["low"]
        high = self.dfdata["high"]
        self.dfdata["Estocastico"] = 100*(close-low)/(high-low)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x = self.dfdata.index, 
                                 y = self.dfdata["Estocastico"], mode='lines'))
        return fig

    # grafico de media movil del precio de cierre
    def avg_graph(self):
        period = 30
        self.dfdata['media_movil'] = self.dfdata['Estocastico'].rolling(window=period).mean()
        self.dfdata['media_movil_close'] = self.dfdata['close'].rolling(window=period).mean()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = self.dfdata.index, 
                                 y = self.dfdata["media_movil"], mode='lines'))
        return fig

    # grafico conjunto de media movil y estocastico
    def mixed_graph(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = self.dfdata.index, 
                                 y = self.dfdata["Estocastico"], 
                                 mode='lines', 
                                 name = 'Estocástico', 
                                 line=dict(color='#0077cc')))
        fig.add_trace(go.Scatter(x = self.dfdata.index, 
                                 y = self.dfdata["media_movil"], 
                                 mode='lines', 
                                 name = 'Media móvil', 
                                 line=dict(color='red', width=2)))

        return fig
    
    # grafico conjunto de media movil y precios de cierre
    def avg_close(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = self.dfdata.index, 
                                 y = self.dfdata["close"], 
                                 mode='lines', 
                                 name= 'Precio de cierre',
                                 line=dict(color='#0077cc')))
        fig.add_trace(go.Scatter(x = self.dfdata.index, 
                                 y = self.dfdata["media_movil_close"], 
                                 mode='lines', 
                                 name = 'Media móvil',
                                 line=dict(color='red', width=2)))

        return fig

    # def sthoc_close(self): 
    #     fig = go.Figure()
    #     fig.add_trace(go.Scatter(x = self.dfdata.index, 
    #                              y = self.dfdata["close"], 
    #                              mode='lines', 
    #                              name= 'Precio de cierre',
    #                              line=dict(color='#0077cc')))
    #     fig.add_trace(go.Scatter(x = self.dfdata.index, 
    #                              y = self.dfdata["Estocástico"], 
    #                              mode='lines', 
    #                              name = 'Estocástico',
    #                              line=dict(color='red', width=2)))