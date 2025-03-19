import mysql.connector

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host="tkp-dev.c7i8g6mwssvi.ap-south-1.rds.amazonaws.com",
    user="admin",  
    password="kaizenadmin123",  
    database="aspirant"  
)

cursor = db_connection.cursor()

# Modified query to select the 'id' along with other columns
query = """
SELECT id, name, description, long_description, job_family, job_family_description, 
       sector, industry, specialisations, keywords 
FROM career_role;
"""

cursor.execute(query)
results = cursor.fetchall()

# Print only the first value of each column in the first row
if results:
    first_row = results[0]
    print(f"ID: {first_row[0]}")
    print(f"Name: {first_row[1]}")
    print(f"Description: {first_row[2]}")
    print(f"Long Description: {first_row[3]}")
    print(f"Job Family: {first_row[4]}")
    print(f"Job Family Description: {first_row[5]}")
    print(f"Sector: {first_row[6]}")
    print(f"Industry: {first_row[7]}")
    print(f"Specialisations: {first_row[8]}")
    print(f"Keywords: {first_row[9]}")

cursor.close()
db_connection.close()
