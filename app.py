from flask import Flask, render_template
import database as dbase
from crearProducto import crear_producto_bp
from editarProducto import editar_producto_bp
import os
from eliminarProducto import eliminar_producto_bp
from buscarFiltrar import buscar_filtrar_bp

db = dbase.dbConnection()

app = Flask(__name__)

app.register_blueprint(buscar_filtrar_bp) 
app.register_blueprint(crear_producto_bp)
app.register_blueprint(editar_producto_bp)
app.register_blueprint(eliminar_producto_bp)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



app.config['UPLOAD_FOLDER2'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS2'] = ALLOWED_EXTENSIONS
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    



@app.route('/')
def home():
    products = db['products']
    productsReceived = list(products.find())
    return render_template('index.html', products=productsReceived)
#hu-05
@app.route('/listar')
# def listar():
#     products = db['products']
#     productsReceived = list(products.find())
#     return render_template('listar.html', products=productsReceived)
def listar():
    products = db['products']
    #filtrar solo damas 
    productsReceived = list(products.find({'categoria': 'Damas'}))
    return render_template('listar.html', productos=productsReceived, query='', category_selected='Damas', min_price='', max_price='')

if __name__ == '__main__':
    app.run(debug=True, port=4000)