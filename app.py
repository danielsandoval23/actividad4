from data.data import * #Importa todas las funciones y variables del módulo data ubicado en el paquete data.
from BD.baseDatos import * #Importa todas las funciones y variables del módulo baseDatos ubicado en el paquete BD.
from sklearn.linear_model import LinearRegression # Importa la clase LinearRegression del módulo linear_model de la biblioteca Scikit-Learn.
from grafica.grafica import *#Importa todas las funciones y variables del módulo grafica ubicado en el paquete grafica. 
import pandas as pd # Importa la biblioteca pandas bajo el nombre "pd".

#Datos del excel #comentario
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico() #Llama a la función dataTeorico() del módulo data para obtener datos teóricos de esfuerzo y deformación. 

#Datos de la base de datos y realizamos el modelo #comentario
data_list = lecturaDatos() #Llama a la función lecturaDatos() del módulo baseDatos para obtener datos reales de una base de datos.
data_real = pd.DataFrame(data_list) #Convierte la lista data_listen un DataFrame de pandas llamado data_real.
data_real_fit = data_real # Crea una copia de la data_real llamada DataFrame data_real_fit.
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1) #Extrae la columna 'Esfuerzo[kN]' del DataFrame y la almacena en la variable X como un arreglo NumPy bidimensional.
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1) # Extrae la columna 'Deformacion[mm]' del DataFrame y la almacena en la variable Y como un arreglo NumPy bidimensional.
x_lim = data_real['Esfuerzo[kN]'].iloc[-1] # Obtiene el último valor de la columna 'Esfuerzo[kN]' del DataFrame data_real y lo almacena en x_lim.
y_lim = data_real['Deformacion[mm]'].iloc[-1] #Obtiene el último valor de la columna 'Deformacion[mm]' del DataFrame data_real y lo almacena en y_lim.
model = LinearRegression() #Crea una instancia de la clase LinearRegression de Scikit-Learn, que se utilizará para entrenar un modelo de regresión lineal.
model.fit(X, y) #Entrena el modelo de regresión lineal utilizando los datos de X(esfuerzo) como características Y y (deformación) como la variable objetivo.
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1) #Realice una predicción utilizando el modelo entrenador, se predice la deformación correspondiente a un esfuerzo de 3000 kN, la predicción se redondea a un decimal y se almacena en la variable prediction.
print('la predicción a 1000 kN es de: ', prediction ,'mm') # imprime "la predicción a 1000 kN es de:" el valor de prediction y "mm"


dataRealEsfuerzo = data_real['Esfuerzo[kN]'] #Extrae la columna 'Esfuerzo[kN]' del DataFrame data_real y la almacena en dataRealEsfuerzo.
dataRealDeformacion = data_real['Deformacion[mm]'] #Extrae la columna 'Deformación[mm]' del DataFrame data_real y la almacena en dataRealDeformacion.

#realizamos la lectura de las gráficas # comentario
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)

#Las anteriores tres líneas llaman a funciones de generación de gráficos que utilizan los datos obtenidos y el modelo entrenado para crear visualizaciones.