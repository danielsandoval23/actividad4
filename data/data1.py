import pandas as pd # Importa la biblioteca pandas y la asigna el nombre "pd".

# Importar datos del csv #comentario
data_teorico = pd.read_csv(r"C:\Users\karen\Downloads\actividad_4\data\Data_ingeniero.csv") #carga datos desde un archivo CSV ubicado en la ruta especificada.

#Código general #comentario
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): #Define una función de llamada dataTeorico().
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]'] #dentro de la función, esta línea crea una variable llamada dataTeoricoEsfuerzo y la asigna a la columna 'Esfuerzo[kN]' del DataFrame data_teorico.
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]'] #crea una variable llamada dataTeoricoDeformacion y la asigna a la columna 'Deformacion[mm]' del DataFrame data_teorico.
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion #devuelve dos resultados: dataTeoricoEsfuerzo y dataTeoricoDeformacion. 


