import mysql.connector

class EmployeManager:
    def __init__(self,  host, user, password, database):
        self._conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def get_employes(self, min_salary=None):
        query = "SELECT * FROM employes"
        if min_salary is not None:
            query += f" WHERE salaire >= {min_salary}"
        cursor = self._conn.cursor()
        cursor.execute(query)
        employes = cursor.fetchall()
        cursor.close()
        return employes

    def get_employes_with_services(self):
        query = "SELECT e.nom, e.prenom, e.salaire, s.nom as service FROM employes e INNER JOIN services s ON e.id_service = s.id"
        cursor = self._conn.cursor()
        cursor.execute(query)
        employes = cursor.fetchall()
        cursor.close()
        return employes

    def insert_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom,prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        cursor = self._conn.cursor()
        cursor.execute(query, values)
        self._conn.commit()
        cursor.close()

    def update_employe_salaire(self, employe_id, nouveau_salaire):
        query = "UPDATE employes SET salaire = %s WHERE id = %s"
        values = (nouveau_salaire, employe_id)
        cursor = self._conn.cursor()
        cursor.execute(query, values)
        self._conn.commit()
        cursor.close()

    def delete_employe(self, employe_id):
        query = "DELETE FROM employes WHERE id = %s"
        values = (employe_id,)
        cursor = self._conn.cursor()
        cursor.execute(query, values)
        self._conn.commit()
        cursor.close()

    def __del__(self):
        self._conn.close()

# Create an instance of EmployeManager and connect to the database
manager = EmployeManager(user = 'root', psswd = '1234', database = 'LaPlateforme')

# Insert a new employe into the database
manager.insert_employe("Doe", "John", 3500, 1)
manager.insert_employe("Doe", "Jane", 3500, 1)
manager.insert_employe("Doe", "Jack", 3500, 1)

# Update the salary of an existing employe
manager.update_employe_salaire(1, 4000)

# Delete an employe from the database
manager.delete_employe(3)

# Retrieve all employes with their services and print their names, salaries, and service names
employes_with_services = manager.get_employes_with_services()
for employe in employes_with_services:
    print(employe[0], employe[1], employe[2], employe[3])


# Retrieve all employes with their services and print their names, salaries, and service names
employes_with_services = manager.get_employes_with_services()
for employe in employes_with_services:
    print(employe)

# Disconnect from the database
del manager