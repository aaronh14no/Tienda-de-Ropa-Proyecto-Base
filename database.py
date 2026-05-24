from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://aaronherbas123321_db_user:A87a94a109a@cluster0.olqxkhn.mongodb.net/?appName=Cluster0'

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
        db = client["dbb_products_app"]
        return db
    except Exception as e:
        print("Error de conexión con la bdd:", e)
        return None