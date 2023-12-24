import streamlit as st
from data import Data
from indicators import Indicators


class App: 
    def __init__(self):
        self.data = Data()
        self.indicators = Indicators()


    def intro_page(self):
        st.header('Introducción')
        st.write("¡Hola! Nos complace darte la bienvenida a nuestro proyecto de la asignatura de Python del Máster en Big Data Science de la Universidad de Navarra.")  
        st.write("En esta aplicación web, exploramos las cotizaciones de diferentes criptomonedas, centrándonos en los pares de divisas y utilizando herramientas de programación en Python.")
        st.write("Nuestro proyecto tiene como objetivo analizar y visualizar la relación entre diferentes monedas a través de sus pares de cotización. Plasmaremos patrones, tendencias y datos históricos para proporcionar una comprensión más profunda del mercado de divisas.")
        st.write("Este proyecto ha sido desarrollado por Inés Hernández y Paula Sanjuan.")    

    def cot_page(self):
        st.header("Cotizaciones")
        st.write('''En esta segunda página se puede ver el gráfico de velas del par seleccionado, además de la base de datos importada con la información de tiempo, apertura, cierre, máximo, mínimo y volumen. ''')

    def ind_page(self):
        st.header("Indicadores")
        st.write("En esta tercera ventana podemos ver la representación gráfica de la cotización del par de monedas, el indicador estocástico, la media móvil del estocástico y finalmente, representaciones conjuntas de las cotizaciones, el estocástico y media movil de ambas.")

    def run(self):
        col1, col2 = st.columns([3, 1])  # La primera columna ocupa 3/4 del ancho, la segunda 1/4
        with col1:
            st.title("Proyecto de Python")
        with col2:
            # Imagen en la esquina superior derecha
            st.image('logo_unav.png', use_column_width=True)
        
        st.sidebar.title("Menú Principal")
        # Create a radio button to navigate between pages
        page = st.sidebar.radio("Selecciona una página: ", ["Introducción", "Cotizaciones", "Indicadores"])
        # Create a container for the main content
        content = st.container()
        # Display content based on the selected page
        with content:
            if page == "Introducción":
                self.intro_page()

                
            elif page == "Cotizaciones":
                self.cot_page()

                criptos = ('ETH/USD','USDT/USD','BTC/USD','XRP/USD','SOL/USD')
                selected_pair = st.selectbox('Selecciona un par de monedas: ', criptos)
                self.data.set_pair_type(selected_pair)

                self.data.get_data(selected_pair)
                data = self.data.data_clean()

                fig = self.data.candle_graph()
                st.header(f'Gráfico de velas del par {selected_pair}')
                st.plotly_chart(fig)
                
                st.write(f'Datos para {selected_pair}: ')
                st.write(self.data.data)

                # st.write(f'Datos de precios de cierre para {selected_pair}: ')
                # st.write(self.data.data_close)

                
            elif page == "Indicadores":
                self.ind_page()
                # self.indicators.set_indicators(data)
                criptos = ('ETH/USD','USDT/USD','BTC/USD','XRP/USD','SOL/USD')
                selected_pair = st.selectbox('Selecciona un par de monedas: ', criptos)
                self.data.set_pair_type(selected_pair)

                self.data.get_data(selected_pair)
                data = self.data.data_clean()

                self.indicators.set_indicators(data)

                st.header(f'Cotización del par {selected_pair}: ')
                fig = self.indicators.line_graph()
                st.plotly_chart(fig)

                st.header(f'Estocástico del par {selected_pair}: ')
                fig2 = self.indicators.stochastic_graph()
                st.plotly_chart(fig2)

                st.header(f'Media móvil del estocástico del par {selected_pair}: ')
                fig3 = self.indicators.avg_graph()
                st.plotly_chart(fig3)

                st.header(f'Gráfico conjunto de la Media móvil del estocástico y el Estocástico del par {selected_pair}: ')
                fig4 = self.indicators.mixed_graph()
                st.plotly_chart(fig4)

                st.header(f'Gráfico conjunto de la Media móvil del precio de cierre y Cotización del par {selected_pair}: ')
                fig5 = self.indicators.avg_close()
                st.plotly_chart(fig5)


                


        


if __name__ == "__main__":
    app = App()
    app.run()


#(venvpython) C:\Users\uah20\Desktop\MBDS\Python\ProyectoPythonInesPaula>streamlit run c:\Users\uah20\Desktop\MBDS\Python\ProyectoPythonInesPaula\main.py