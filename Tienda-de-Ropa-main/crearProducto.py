from flask import Blueprint, request, jsonify, redirect, url_for, current_app 
from product import Product
import database as dbase
import os
from werkzeug.utils import secure_filename

db = dbase.dbConnection()

crear_producto_bp = Blueprint('crear_producto_bp', __name__)

def allowed_file(filename):
    extensions = current_app.config.get('ALLOWED_EXTENSIONS2', {'png', 'jpg', 'jpeg', 'gif'})
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extensions

@crear_producto_bp.route('/products', methods=['POST'])
def addProduct():
    # Usamos tu colección definitiva en MongoDB
    products = db['products']
    
    # 1. Recibimos el nombre original que escribió el usuario en el formulario
    original_name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    stock = request.form.get('stock')
    category = request.form.get('category')

    # 2.cloud
    palabra_antes = "cloud_"
    if original_name:
        name = f"{palabra_antes}{original_name}" # Ejemplo: "tennis" -> "cloud_tennis"
    else:
        name = original_name

    image_name = '' 
    
    if 'image' in request.files:
        file = request.files['image']
        
        if file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = current_app.config['UPLOAD_FOLDER2']
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)
                
            save_path = os.path.join(upload_path, filename)
            file.save(save_path)
            image_name = filename

  
    if name and description and price and stock and category:
        product = Product(name, description, price, stock, category, image_name)
        products.insert_one(product.toDBCollection())

        # Redirige directo a la tabla de productos para ver el cambio
        return redirect(url_for('listar'))
    
    return jsonify({'message': 'Datos incompletos'}), 400