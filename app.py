from flask import Flask, render_template
import database as dbase
from crearProducto import crear_producto_bp
import os

from buscarFiltrar import buscar_filtrar_bp # Importar el blueprint de búsqueda y filtrado


db = dbase.dbConnection()

app = Flask(__name__)

app.register_blueprint(buscar_filtrar_bp) 

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER2'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS2'] = ALLOWED_EXTENSIONS
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.register_blueprint(crear_producto_bp)

@app.route('/')
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products=productsReceived)

@app.route('/listar')
def listar():
    products = db['products']
    productsReceived = products.find()
    return render_template('listar.html', products=productsReceived)

if __name__ == '__main__':
    app.run(debug=True, port=4000)