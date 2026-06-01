from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost:27017/tu_base_de_datos'

def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        db = client["dbb_products_app"]
        return db
    except Exception as e:
        print("Error de conexión con la bdd:", e)
        return None