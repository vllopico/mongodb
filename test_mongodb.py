from pymongo import MongoClient

try:
	cataleg = MongoClient('localhost', 27017)
except:
	print("No podem connectar amb MongoDb")
	

def print_comanda(comanda):
	linees = []
	for c in comanda:
		print("-----------------------------------------------------")
		print("Comanda: ", c["ref"], " - ", c["client"])
		print("-----------------------------------------------------")
		linees = c["linies"]
		for l in linees:
			print("\t", l['linia'], "  ", l["article"], " ", l["format"], " ", l["preu"], "€ ", l["pes"], "Kg" )
	print("-----------------------------------------------------")


db = cataleg.catalogo
comanda = db.comanda

#dades a insertar
com_1 = {
	"ref":3, 
	"client":"E_000003", 
	"linies":
		[
			{"linia":1,"article":"producte_4", "format":"S", "preu": 12, "pes":1},
			{"linia":2,"article":"producte_3", "format":"P", "preu": 2, "pes":14}
			
		]
}

com_2 = {
	"ref":4, 
	"client":"E_000003", 
	"linies":
		[
			{"linia":1,"article":"producte_12", "format":"S", "preu": 132, "pes":13},
			{"linia":2,"article":"producte_33", "format":"P", "preu": 23, "pes":134}
			
		]
}


#insertar nous documents
comanda.insert_one(com_1)
comanda.insert_one(com_2)


#Visualització de tota la colecció
comd = comanda.find()
print_comanda(comd)


#consultes, amb find
print("Documents del client: E_000003" )
com_busc = comanda.find({"client": "E_000003"})
print_comanda(com_busc)


	
