from pymongo import MongoClient

# Dejamos la URI armada de forma genérica para que no rebote tu contraseña real en el GitHub del grupo
MONGO_URI = 'mongodb+srv://aaronherbas123321_db_user:A87a94a109a@cluster0.olqxkhn.mongodb.net/?appName=Cluster0'

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client["dbb_products_app"]
        return db
    except Exception as e:
        print("Error de conexión con la bdd:", e)
        return None