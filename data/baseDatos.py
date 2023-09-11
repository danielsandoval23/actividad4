from pymongo.mongo_client import MongoClient #Esta línea importa la clase.

#CONEXIÓN #comentario.
def conexion(): #Define una función de llamada conexion() que se utilizará para establecer la conexión con la base de datos MongoDB.
    uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"
    #Esta línea define una cadena de conexión URI que contiene la información necesaria para conectarse a la base de datos MongoDB.
    # Create a new client and connect to the server
    return MongoClient(uri) #Esta línea crea una instancia de MongoClient utilizando la URI de conexión definida en la línea anterior y la devuelve como resultado de la función conexion(),esto establece la conexión a la base de datos cuando se llama a la función conexion().

#CREATE #comentario.
""" Código necesario para crear un create en MongoDB"""


#READ #comentario.
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos(): #Define una función llamada lecturaDatos() que se utilizará para realizar operaciones de lectura en la base de datos MongoDB.
    client = conexion() #Llama a la función conexion() para obtener una instancia de MongoClient y la asigna a la variable client, lo que establece la conexión a la base de datos.
    db = client.actividad4.data_real #Accede a la base de datos llamada actividad4 y a la colección llamada data_real dentro de esa base de datos.
    data_list = [] #Crea una lista vacía de llamada data_list que se utilizará para almacenar los documentos recuperados de la colección.
    for data_real_bd in db.find(): #itera a través de todos los documentos en la colección data_real y los almacenados en la lista data_list utilizando data_list.append(data_real_bd).
        data_list.append(data_real_bd) #itera a través de todos los documentos en la colección data_real y los almacenados en la lista data_list utilizando data_list.append(data_real_bd).
    return data_list 
    # Devuelve la lista de datalist.

#UPDATE #comentario.
""" Código necesario para actualizar un dato en la BD"""

#DELETE #comentario.
""" Código necesario para eliminar un dato en la BD"""