import pandas as pd #Importa la biblioteca pandas y la asigna a un nombre 'pd' para facilitar su uso en el código.

# Importar datos del csv #comentario.
data_teorico = pd.read_csv(r"C:\Users\karen\Downloads\actividad_4\data\Data_ingeniero.csv") #Lee un archivo CSV ubicado en la ruta especificada y almacena los datos en un objeto DataFrame llamado data_teorico. 

#Código general #comentario.
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): #Define una función llamada dataTeorico().
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]'] #Crea una nueva variable llamada dataTeorico Esfuerzo y la asigna a la columna 'Esfuerzo[kN]' del DataFrame data_teorico, esto extrae los valores de esa columna y los almacena en la variable.
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]'] #Crea una nueva variable llamada dataTeorico Deformacion y la asigna a la columna 'Deformacion[mm]' del DataFrame data_teorico, esto extrae los valores de esa columna y los almacena en la variable.
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion # Devuelve las dos variables dataTeorico Esfuerzo y dataTeorico Deformacion.


