import csv
import psycopg2

conn = psycopg2.connect(database="Friendship", user = "postgres", password = "newPassword", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
cur.execute("select * from ratings;")
rows = cur.fetchall()
users = 220970
arr = [{} for i in range(users+1)]

for row in rows:
	a,b,c = int(row[0]), int(row[1]), int(row[2])
	arr[a][b] = c
	arr[b][a] = c
	
def sim(x, y):
	common = 0
	uncommon = 0
	v = arr[x].keys()[:70]
	for i in v:
		temp = arr[y].get(i)
		if temp != None:
			temp2 = arr[x][i]
			if abs(temp - temp2) <= 1:
				common += 1
			else:
				uncommon += 1
	if common + uncommon == 0:
		return 0
	val = float(common)/(common + uncommon)
	return val

def rate(x, y):
	pred = 0.0
	si = 0.0
	temp = arr[y].items()
	for i in temp[:40]:
		val = sim(x, i[0])
		pred += val*i[1]
		si += val

	if si == 0:
		return 5
	else:
		return pred/si

pred = []
with open("test_user_ratings.csv", "rb") as f:
	reader = csv.reader(f)
	flag = True
	for row in reader:
		if(flag):
			flag = False
			continue
		a,b = int(row[0]), int(row[1])
		pred.append([a,b])

rating = []
for i in range(len(pred)):
	exp = rate(pred[i][0], pred[i][1])
	rating.append(exp)

with open("Fin5.csv", "w") as f:
	reader = csv.writer(f)
	reader.writerow(["Rating"])
	for i in rating:
		reader.writerow([str(int(i))])
