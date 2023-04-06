import mysql.connector

# create a connection to the database
ma_bdd = mysql.connector.connect(  user = 'root', psswd = '1234', database = 'LaPlateforme' )
print(ma_bdd)

# create a cursor pour éxecutet des requêtes SQL
mon_curseur = ma_bdd.cursor()

#  Run the SQL query to retrieve all students 
mon_curseur.execute("SELECT * FROM Etudiant")

# Get the result of the query
resultat = mon_curseur.fetchall()

# Print the result of the query
for (id, nom, prenom, age, email) in resultat:
    print(f'ID: {id}, \nNom: {nom}, \nPrénom: {prenom}, \nAge: {age}, \nEmail: {email}')

# Close the cursor and the connection
mon_curseur.close()
ma_bdd.close()