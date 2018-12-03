from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import math
import csv
import random
import _pickle as cPickle
import dill


try:
	conn = connect("dbname='postgres' user='xyz' host='localhost' password='123'")
except:
	print("Failed to connect to the target database.")

users = {}
testCSV = open('test_user_ratings.csv')	
readCSV = csv.reader(testCSV, delimiter=',')
for i, row in enumerate(readCSV):
	if i == 0:
		continue
	users[int(row[0])] = 1
	users[int(row[1])] = 1


conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
#userSet = repr(users).replace('{', '(').replace('}', ')')
cur.execute("SELECT * From ratings")
records = cur.fetchall()

 

userFriends = {}
for record in records:
	if record[0] not in users:
		if record[0] not in userFriends:
			userFriends[record[0]] = {"avg": 0, "count": 0}
		currSum = userFriends[record[0]]["avg"] * userFriends[record[0]]["count"] + record[2]
		userFriends[record[0]]["count"] += 1
		userFriends[record[0]]["avg"] = currSum/userFriends[record[0]]["count"]
	if record[1] not in users:
		if record[1] not in userFriends:
			userFriends[record[1]] = {"avg": 0, "count": 0}
		
		currSum = userFriends[record[1]]["avg"] * userFriends[record[1]]["count"] + record[2]
		userFriends[record[1]]["count"] += 1
		userFriends[record[1]]["avg"] = currSum/userFriends[record[1]]["count"]

	if record[0] in users:
		if record[0] not in userFriends:
			userFriends[record[0]] = {"avg": 0}
		userFriends[record[0]][record[1]] = record[2]
		userFriends[record[0]]["avg"] = (userFriends[record[0]]["avg"]*(len(userFriends[record[0]])-2)+record[2])/(len(userFriends[record[0]]) - 1)

	if record[1] in users:
		if record[1] not in userFriends:
			userFriends[record[1]] = {"avg": 0}
		userFriends[record[1]][record[0]] = record[2]
		userFriends[record[1]]["avg"] = (userFriends[record[1]]["avg"]*(len(userFriends[record[1]])-2)+record[2])/(len(userFriends[record[1]]) - 1)
		

def ld_writeDicts(filePath,dict):
	f=open(filePath,'wb')
	newData = cPickle.dumps(dict, 1)
	f.write(newData)
	f.close()

ld_writeDicts('test2.dta',userFriends)
	

# read file decoding with cPickle/pickle (as binary)
def ld_readDicts(filePath):
	f=open(filePath,'rb')
	data = cPickle.load(f)
	f.close()
	return data

# return dict data to new dict
userFriends = ld_readDicts('test2.dta')




'''
pickle_out = open("dict.pickle","wb")
dill.dump(userFriends, pickle_out)
pickle_out.close()
'''

#del records
del users
cc = 0
def getRating(F1, F2):
#	cur = conn.cursor()
	global cc

	if F1 not in userFriends:
		print(F1, "not found")
		return 0
	if F2 not in userFriends:
		return 0
		#return 0;
		
	#print(userFriends[fri])
	ratings = 0
	denom = 0
	for friend, rating in userFriends[F1].items():
		if friend in userFriends[F2]:
			if friend == "avg" or friend == "count":
				continue
			ratings += (userFriends[F2][friend] - userFriends[friend]["avg"])*1
#			denom += userFriends[F1][friend]
			denom += 1

 
	if (denom == 0):
		return userFriends[F1]["avg"]
	ratings = userFriends[F1]["avg"] +  ratings/denom
	#print(round(ratings))
	#cur.close()
	cc += 1
	if cc % 10000 == 0:
		print(cc)
	return round(ratings)

	totalUser1Ratings = math.sqrt(totalUser1Ratings)
	 ƒ

	cur.execute("SELECT * From ratings where userid="+str(F2)+" or profileid="+str(F2))
	records2 = cur.fetchall()
	totalUser2Ratings = 0	
	for record in records2:
		totalUser2Ratings += record[2]*record[2]
		friendPos = 1
		if(record[friendPos] == F2):
			friendPos = 0	
		friendId = record[friendPos]
		if friendId in user1Friends:
			ratings += user1Friends[friendId] * record[2]
		

	totalUser2Ratings = math.sqrt(totalUser2Ratings)

#print(getRating(16607, 158746))
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																															
																																																						

csvfile = open('test4.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow(["Rating"])


testCSV = open('test_user_ratings.csv')	
readCSV = csv.reader(testCSV, delimiter=',')

for i, row in enumerate(readCSV):
	if i == 0:
		continue
	writer.writerow([int(getRating(int(row[0]), int(row[1]) ))])