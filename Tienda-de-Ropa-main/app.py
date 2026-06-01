from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase  
import filters
import os

db = dbase.dbConnection()
app = Flask(__name__)

# --- CONFIGURACIÓN DE CARPETAS (RUTA ABSOLUTA) ---
# Esto obtiene la ruta real de tu carpeta de proyecto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')

app.config['UPLOAD_FOLDER2'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS2'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

# Asegurar que la carpeta exista
if not os.path.exists(app.config['UPLOAD_FOLDER2']):
    os.makedirs(app.config['UPLOAD_FOLDER2'])
# ------------------------------------------------

# Importación de Blueprints (Importarlos después de configurar app.config)
from crearProducto import crear_producto_bp
from editarProducto import editar_producto_bp
from eliminarProducto import eliminar_producto_bp

app.register_blueprint(crear_producto_bp)
app.register_blueprint(editar_producto_bp, url_prefix='/productos')
app.register_blueprint(eliminar_producto_bp, url_prefix='/productos')

@app.route('/')
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)

@app.route('/listar')
def listar():
    products = db['products']
    productsReceived = products.find()
    return render_template('listar.html', products = productsReceived)

@app.route('/filtrosbusqueda')
def filtrosbusqueda():
    products = db['products']
    
    query = filters.build_filter_query() 
    
    all_categories = products.distinct("categoria") 
    
    productsReceived = list(products.find(query)) 
    
    return render_template(
        'filtrosbusqueda.html',
        products=productsReceived,
        categories=all_categories
    )
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)