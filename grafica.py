import matplotlib.pyplot as plt #importa matplotlib
import numpy as np #importa numpy



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
    #Esta línea define una función llamada gr_con_prediccion que toma seis argumentos: x_lim, y_lim, dataTeoricoEsfuerzo, dataTeoricoDeformacion, dataRealEsfuerzo, y dataRealDeformacion.
    
    plt.figure(figsize=(15, 6)) #Esta línea crea una figura para la gráfica con un tamaño específico de 15 unidades de ancho y 6 unidades de alto.
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Esta línea traza una línea conectando los puntos definidos por dataTeoricoEsfuerzo en el eje x y dataTeoricoDeformacion en el eje y. 
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red') #Esta línea agrega puntos dispersos (diagrama de dispersión) en rojo para los datos representados por dataRealEsfuerzo en el eje x y dataRealDeformacion en el eje y. 
    plt.xlabel('Esfuerzo [kN]') #Esta línea establece etiqueta para el eje x de la gráfica.
    plt.ylabel('Deformación [mm]') #Esta línea establece etiqueta para el eje y de la gráfica.
    plt.title('Gráfica 2: teórico versus real [ZOOM]') #Esta línea establece un título para la gráfica.
    plt.xlim(0, x_lim) #Esta línea establece los límites para el eje x de la gráfica, utilizando los valores proporcionados en el argumento x_lim.
    plt.ylim(0, y_lim) #Esta línea establece los límites para el eje y de la gráfica, utilizando los valores proporcionados en el argumento y_lim.
    plt.grid() #Esta línea agrega una cuadrícula a la gráfica.
    plt.gca().invert_yaxis() # Esta linea invierte los valores en el eje y para que los mas grandes salgan abajo y los menores arriba.
    plt.show() #Esta línea muestra la gráfica en pantalla.

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model): ##Esta línea define una función llamada gr_con_prediccion_3000 que toma los argumentos: prediction,model, x_lim, y_lim, dataTeoricoEsfuerzo, dataTeoricoDeformacion, dataRealEsfuerzo, y dataRealDeformacion.
  plt.figure(figsize=(15, 6)) #Esta línea crea una figura para la gráfica con un tamaño específico de 15 unidades de ancho y 6 unidades de alto.
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Esta línea traza una línea conectando los puntos definidos por dataTeoricoEsfuerzo en el eje x y dataTeoricoDeformacion en el eje y. 
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #Esta línea agrega puntos dispersos (diagrama de dispersión) en rojo para los datos representados por dataRealEsfuerzo en el eje x y dataRealDeformacion en el eje y.
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m') #Esta línea traza una línea magenta que representa la predicción del modelo en un rango de esfuerzo de 0 a 1000 kN.
  plt.scatter(	3000 , prediction, color='green') #Esta línea agrega un punto verde en la gráfica que representa la predicción a una carga de 3000 kN.
  plt.xlabel('Esfuerzo [kN]') #Esta línea establece etiqueta para el eje x de la gráfica.
  plt.ylabel('Deformación [mm]') #Esta línea establece etiqueta para el eje y de la gráfica.
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN') #Esta línea establece un título para la gráfica.
  plt.xlim(0, 3000) #Esta línea establece los límites para el eje x de la gráfica.
  plt.ylim(0, 45) #Esta línea establece los límites para el eje y de la gráfica.
  plt.grid()#Esta línea agrega una cuadrícula a la gráfica.
  plt.gca().invert_yaxis() # Esta linea invierte los valores en el eje y para que los mas grandes salgan abajo y los menores arriba.
  plt.show() #Esta línea muestra la gráfica en pantalla.

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #Esta línea define una función llamada gr_sin_prediccionque toma cuatro argumentos, que son los datos teóricos y reales de esfuerzo y deformación.
  plt.figure(figsize=(15, 6)) #Esta línea crea una figura para la gráfica con un tamaño específico de 15 unidades de ancho y 6 unidades de alto.
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Esta línea traza una línea conectando los puntos definidos por dataTeoricoEsfuerzo en el eje x y dataTeoricoDeformacion en el eje y. 
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #Esta línea agrega puntos dispersos (diagrama de dispersión) en rojo para los datos representados por dataRealEsfuerzo en el eje x y dataRealDeformacion en el eje y.
  plt.xlabel('Esfuerzo [kN]')#Esta línea establece etiqueta para el eje x de la gráfica.
  plt.ylabel('Deformación [mm]') #Esta línea establece etiqueta para el eje y de la gráfica.
  plt.title('Gráfica 1: teórico versus real') #Esta línea establece un título para la gráfica.
  plt.grid() #Esta línea agrega una cuadrícula a la gráfica.
  plt.gca().invert_yaxis() # Esta linea invierte los valores en el eje y para que los mas grandes salgan abajo y los menores arriba.
  plt.show() #Esta línea muestra la gráfica en pantalla.
