# PASO 1: Importar el módulo "mysql.connector" previamente ¡INSTALADO!
import mysql.connector

data = []

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_banco")
        return connection

    def insert_db(self, n_cuenta, id_usuario, edad, nombre_apellido,contrasena):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_usuarios(N_CUENTA, ID_USUARIO, EDAD,NOMBRE_APELLIDO, CONTRASENA) VALUES (%s,%s,%s,%s,%s)"
        data = (n_cuenta, id_usuario, edad, nombre_apellido,contrasena)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()

    def read_db(self):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "SELECT N_CUENTA, ID_USUARIO, EDAD,NOMBRE_APELLIDO, CONTRASENA FROM TBL_USUARIOS"
        cursor.execute(query)
        registro = 0
        for fila in cursor:
            data.append(fila) 
            print(str(registro) +" - "+ str(data[registro]))
            registro = registro + 1 
        
        my_connection.close()     
        #print(data)

    def delete_db(self):
        my_connection = self.open_connection()   
        cursor = my_connection.cursor()  
        query = "DELETE ...."
        cursor.execute(query)
