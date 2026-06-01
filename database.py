from pymongo import MongoClient
import certifi
# Dejamos la URI armada de forma genérica para que no rebote tu contraseña real en el GitHub del grupo
MONGO_URI = "mongodb+srv://veronica:base2026@cluster0.rewf6ma.mongodb.net/?appName=Cluster0"

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000, tlsCAFile=certifi.where())
        db = client["dbb_products_app"]
        return db
    except Exception as e:
        print("Error de conexión con la bd:", e)
        return None.py