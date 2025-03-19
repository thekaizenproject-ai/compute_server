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
query = """SELECT id, name, description, long_description, job_family, job_family_description, 
       sector, industry, specialisations, keywords, desired_facets, soft_skills, hard_skills
FROM career_role;
"""

cursor.execute(query)
results = cursor.fetchall()

# Initialize the list to store the career role data
career_roles = []
for row in results:
    career_roles.append({
        "id": row[0],  # The 'id' is stored in the first column
        "name": row[1],
        "description": row[2],
        "long_description": row[3],
        "job_family": row[4],
        "job_family_description": row[5],
        "sector": row[6],
        "industry": row[7],
        "specialisations": row[8],
        "keywords": row[9],
        "desired_facets": row[10],  # Add desired_facets to the dictionary
        "soft_skills": row[11],     # Add soft_skills to the dictionary
        "hard_skills": row[12]     # Add hard_skills to the dictionary
    })

# Write the career_roles list to a Python file with UTF-8 encoding
with open("roles1.py", "w", encoding="utf-8") as file:
    file.write("career_roles = ")
    file.write(str(career_roles))

# Close the cursor and database connection
cursor.close()
db_connection.close()
