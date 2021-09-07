import sqlite3


def saveBerth(berthName,berthTonnes,berthCalls):
	conn = sqlite3.connect('berthScheduler')

	c = conn.cursor()

	#Create table
	# c.execute("""CREATE TABLE beths (
	# 	berth text,
	# 	total_tonnes integer,
	# 	number_of_calls integer
	# 	)
	# 	""")

	# c.execute("""CREATE TABLE period (
	# 	period integer
	# 	)
	# 	""")

	c.execute("SELECT 1 from beths where berth = ?",(berthName,))

	record_exists = c.fetchone()

	print("Saving berth "+berthName+" | "+berthTonnes+" | "+berthCalls+" | ")

	if record_exists is None:
		print("It does not exist")
		c.execute("INSERT into beths VALUES (?,?,?)",(berthName,berthTonnes,berthCalls))

		conn.commit()
	else:
		print("It exists")

	print(record_exists)
	pass

def getBerths():
	conn = sqlite3.connect('berthScheduler')

	c = conn.cursor()

	c.execute("SELECT *,oid from beths")

	records = c.fetchall()

	return records

def delete_berth(berth):
	conn = sqlite3.connect('berthScheduler')

	c = conn.cursor()

	print("berth is ")
	print(berth)


	c.execute("DELETE from beths where oid = ?",(berth,))

	conn.commit()

