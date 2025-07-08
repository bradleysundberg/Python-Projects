import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('file_list.db')
cur = conn.cursor()

# Create the table with an auto-incrementing ID and a filename text field
cur.execute('''
    CREATE TABLE IF NOT EXISTS TextFiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT
    )
''')

# Tuple of file names
fileList = ('information.docx','Hello.txt','myImage.png', 
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# Loop through the tuple and insert only the .txt files into the database
for file in fileList:
    if file.lower().endswith('.txt'):
        cur.execute("INSERT INTO TextFiles (filename) VALUES (?)", (file,))

# Commit changes to save data
conn.commit()

# Fetch and display all text file records
print("Text files stored in the database:")
cur.execute("SELECT * FROM TextFiles")
rows = cur.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Filename: {row[1]}")

# Close the connection
conn.close()
