from pymongo import MongoClient
import csv
import json

with open('info.csv') as data_csv:
	csv_info = csv.reader(data_csv, delimiter=';')
	
	first_row = next(csv_info)
	first_c1 = first_row[0]
	first_c2 = first_row[1]
	
	first_l1 = first_row[2]
	first_l2 = first_row[3]
	first_l3 = first_row[4]
	first_l4 = first_row[5]
	first_l5 = first_row[6]
	
	info = []
	item_json = {"c1":first_c1, "c2":first_c2, "lines":[[first_l1,first_l2,first_l3,first_l4,first_l5]]}
	
	num_line = 0
	for line in csv_info:
		
		c1 = line[0]
		c2 = line[1]
		l1 = line[2]
		l2 = line[3]
		l3 = line[4]
		l4 = line[5]
		l5 = line[6]
		
		if (first_c1 != c1 or first_c2 != c2):
			info.append(item_json)
			item_json = {"c1":c1, "c2":c2, "lines":[[l1,l2,l3,l4,l5]]}
		else:
			item_json["lines"].append([l1,l2,l3,l4,l5])			
		
		first_c1 = c1
		first_c2 = c2
			
		num_line += 1
	
	#Afegim ultim item del json
	info.append(item_json)

json_data = json.dumps(info)
#Imprimim el json construit
print(json.dumps(info,indent=4,sort_keys=True))


#Connexió amb MongoDb
try:
	bbdd_mongo = MongoClient('localhost', 27017)
except:
	print("No podem connectar amb MongoDb")

db = bbdd_mongo.catalogo
info_bbdd = db.exemple_info

info_mongo = json.loads(json_data)
for row in info_mongo:
	info_bbdd.insert_one(row)
	
