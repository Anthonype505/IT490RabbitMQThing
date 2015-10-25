from pymongo import MongoClient
import hashlib

class MongoThing:
	
	
	def __init__(self):
		site = "mongodb://testadmin:12adam12@ds041633.mongolab.com:41633/it420"
		self.client = MongoClient(site)

	def auth(self, data): #Needs 1 array with two elements: 0 = username  1 = password
		db = self.client["it420"]
		collection  = db.users
		passy = hashlib.sha1(data[1]).hexdigest()
		result = collection.find_one({'username':data[0],'passwd': passy})
		self.client.close()
		if str(result) != "None":
			return True
		else:
			return False
		
	def regi(self,data): #Needs 1 array with 3 elements: 0 = username  1 = password  2 = powerlevel
		db = self.client["it420"]
		collection = db.users
		passy = hashlib.sha1(data[1]).hexdigest()
		post = {"username":data[0],
			"passwd":passy,
			"powerlevel":data[2] }
		post_id = collection.insert_one(post).inserted_id
		self.client.close()
	
	def pull(self,data): #Needs 1 string, which is owner. Owners is usually the username, So when data is sent to the back end, make sure to include the username of the person somehow
		db= self.client["it420"]
		collection = db.games
		thing = collection.find_one({'owner':'agoldman'})
		self.client.close()
		return thing['Titles']
	

