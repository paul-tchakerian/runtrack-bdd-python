import mysql.connector

# create a connection to the database
connexion = mysql.connector.connect(user = 'root', password = '1234', database = 'LaPlateforme')


# create a cursor pour éxecutet des requêtes SQL
mon_curseur = connexion.cursor()

#  Run the SQL query to retrieve all students 
mon_curseur.execute("SELECT * FROM Etudiant")

# excecute
query = "SELECT nom, capacites FROM salles"
mon_curseur.execute(query)

for (nom, capacites) in mon_curseur:
    print(f"Salles: {nom}, Capacités: {capacites}".format(nom, capacites))

# Close the cursor and the connection
mon_curseur.close()
connexion.close()