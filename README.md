# Proyecto de Python: Análisis de Cotizaciones y Oscilador Estocástico en Kraken

Las alumnas del máster en Big Data Science de la Universidad de Navarra Paula Sanjuan Campos e Inés Hernández Pastor hemos creado este proyecto cuyo objetivo principal es la descarga y visualización de cotizaciones para un par de monedas. Todo ello se logra mediante el uso de Python y Streamlit. 


## Herramientas utilizadas

### 1. Python

### 2. Kraken API

La API de Kraken se utiliza para la descarga de datos de cotizaciones actualizados. 

### 3. Streamlit 

La interfaz de usuario ha sido creada con Streamlit, una biblioteca de Python que facilita la creaciónb de aplicaciones web interactivas. Permite seleccionar un par de criptomonedas entre seis posibles en nuestro proyecto, y visualizar las cotizaciones e indicadores. 

### 4. Entorno Virtual 

Hemos configurado un entorno virtual específico para este proyecto utilizando virtualenv. Esto asegura que las dependencias y versiones de las bibliotecas utilizadas sean coherentes y evita posibles conflictos con otros proyectos.



## Instrucciones de configuración

### 1. Descarga desde GitHub

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/tu_proyecto.git
   cd tu_proyecto
2. Configurar el Entorno Virtual

    ```
    virtualenv venv
    # Para Mac: 
    source venv/bin/activate
    # Para Windows:
    venv/Scripts/activate
3. Instalar dependencias 

    ```
    pip install -r requirements.txt
    streamlit run app.py
## Funcionalidades Principales

### Interfaz de usuario

En la parte izquierda de la vista que se abre en el navegador está el índice en el que se selecciona la vista que se quiere visualizar: 'Introducción', 'Cotizaciones' e 'Indicadores'. 

### 1. Descarga de Cotizaciones

El proyecto permite descargar las cotizaciones actualizadas de la plataforma Kraken para el par de monedas seleccionado por el usuario. La información descargada será la base para el análisis posterior.

En la vista de 'Cotizaciones' se selecciona el par a representar.

### 2. Gráficas de Movimiento

Una vez se hayan descargado las cotizaciones, se podrá visualizar fácilmente el movimiento histórico del par de monedas mediante un gráfico de velas. Esta representación gráfica facilitará la identificación de patrones y tendencias en el comportamiento de las cotizaciones.

En la misma vista de 'Cotizaciones', una vez se selecciona el par se puede observar directamente el gráfico de velas y justo debajo el Dataframe en el que se basa la representación. 

### 3. Oscilador Estocástico

Adicionalmente, el proyecto incluirá la generación de gráficas del oscilador estocástico, un indicador técnico ampliamente utilizado en el análisis técnico. Esta herramienta proporcionará insights sobre la posible sobrecompra o sobreventa del par de monedas, ayudándote a tomar decisiones informadas.

El la vista de 'Indicadores' se selecciona de nuevo el par de monedas y se puede observar la cotización del par (precio de cierre en el tiempo), el indicador estocástico y la media móvil del estocástico. Además, se visualiza una gráfica combinada de los anteriores para visualizarlos de forma simultánea. Finalmente, se representa la cotización sobre su media móvil. 



