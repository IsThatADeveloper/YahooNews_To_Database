import sqlite3
import os

file = ('webscrap.db')
if(os.path.exists(file)):
    print('Database has sucessfully been updated')
else:
    conn = sqlite3.connect('webscrap.db')
    c = conn.cursor()
    print('Database has sucessfully been created')
    
    c.execute("""CREATE TABLE webscrap (
        title text,
        about text
    )""")


conn = sqlite3.connect('webscrap.db')
c = conn.cursor()

# Create a Table (DEPENDS ON WEBSCRAP)

# # Commit our command
conn.commit()

# # Close our connection
conn.close()

def show_all():
    conn = sqlite3.connect('webscrap.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM webscrap")

    items = c.fetchall()

    for item in items: 
        print(item)

    conn.commit()
    conn.close()

# ADD A RECORD FUNCTION (NEW RECORD TO TABLE)
def add_one(title, about):
    conn = sqlite3.connect('webscrap.db')
    c = conn.cursor()
    c.execute("INSERT INTO webscrap VALUES (?,?)", (title, about))

    conn.commit()
    conn.close()
    print('Sucessfully added', title, about)

# ADD MANY TO LIST TABLE
def add_many(titles, abouts):
    conn = sqlite3.connect('webscrap.db')
    c = conn.cursor()
    data = [(title, about) for title, about in zip(titles, abouts)]
    c.executemany("INSERT INTO webscrap VALUES (?, ?)", data)
    conn.commit()
    conn.close()
    print('Successfully added', len(titles), 'records')


# ADD A RECORD FUNCTION (NEW RECORD TO TABLE)
def delete_one(id):
    conn = sqlite3.connect('webscrap.db')
    c = conn.cursor()
    c.execute("DELETE from webscrap WHERE rowid = (?)", (id,))
    
    conn.commit()
    conn.close()
    print('Sucessfully deleted', id)

# WHERE CLAUSE ID
def where_id(id):
    conn = sqlite3.connect('webscrap.db')
    c = conn.cursor()
    c.execute("SELECT * from webscrap WHERE rowid = (?)", (id,))
    items = c.fetchall()

    for item in items: 
        print(item)
    
    conn.commit()
    conn.close()

# WHERE CLAUSE EMAIL
def where_id(email):
    conn = sqlite3.connect('webscrap.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from webscrap WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items: 
        print(item)
    
    conn.commit()
    conn.close()
