import mysql.connector

class MySQLDatabase:
    host = "localhost:3306"
    user = "root"
    password = "1234"
    database = "tunning"
    connection = None
    cursor = None
    
    def __init__(self, host, user, password, database):
        """Initialize the MySQLDatabase object and establish the connection."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establish a connection to the database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connection established successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def execute_query(self, query, params=None):
        """Execute a query and return the result if applicable."""
        try:
            self.cursor.execute(query, params)
            # Commit for DML (INSERT, UPDATE, DELETE)
            if query.strip().lower().startswith(('insert', 'update', 'delete')):
                self.connection.commit()
                print("Query executed successfully.")
            else:
                # Return fetched results for SELECT queries
                return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def close(self):
        """Close the database connection and cursor."""
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
        print("Connection closed.")