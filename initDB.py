import sqlite3

'''
-------------------------------------------
sqlite3 gesture
-------------------------------------------
'''

def configDb():
	conn = sqlite3.connect('posts.db')
	c = conn.cursor()
	return [conn,c]

def closeDb(conn, c):
	try:
		c.commit()
		conn.close()
		return True
	except:
		return False

'''
-------------------------------------------
Create Tables
-------------------------------------------
'''
		
def createPostsTable():
	try:
		c.execute('''CREATE TABLE posts (user integer, content text, date integer)''')
		return True
	except:
		return False

if __name__ == "__main__":
	# Create the DB
	[conn, c] = configDb()
	if(createPostsTable()==True):
		print("Correctly created the table")
	else:
		print("Error while creating the table")
	
	closeDb(conn, c)