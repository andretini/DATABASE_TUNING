import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',      # Altere para o seu host
            database='tunning',    # Altere para o seu banco de dados
            user='root',      # Altere para o seu usuário
            password='1234'    # Altere para a sua senha
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
