from flask import Blueprint, request, jsonify, redirect, url_for, current_app
import database as dbase
import os
from werkzeug.utils import secure_filename

db = dbase.dbConnection()

crear_producto_bp = Blueprint('crear_producto_bp', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS2']

@crear_producto_bp.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    
    # 1. Capturar textos del formulario
    name = request.form.get('name', '').strip()
    description = request.form.get('description', '').strip()
    category = request.form.get('category', '').strip()

    # 2.VALIDACIONES DE SEGURIDAD 
    if not name or not description or not category:
        return jsonify({'message': 'Campos obligatorios incompletos'}), 400

    # HU-09: Validación de Precio Numérico
    try:
        price = float(request.form.get('price', 0))
    except ValueError:
        return jsonify({'message': 'El precio debe ser un número válido'}), 400

    # HU-09: Validación de Stock (Entero y No Negativo)
    try:
        stock = int(request.form.get('stock', 0))
        if stock < 0:
            return jsonify({'message': 'El stock no puede ser negativo'}), 400
    except ValueError:
        return jsonify({'message': 'El stock debe ser un número entero'}), 400

    #  Procesamiento de la Imagen (Subida local de archivos)
    image = ''
    if 'image' in request.files:
        file = request.files['image']
        if file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(current_app.config['UPLOAD_FOLDER2'], filename)
            file.save(save_path)
            image = filename

    # 6. GUARDADO EN ESPAÑOL DIRECTO A MONGO ATLAS
    nuevo_producto = {
        'nombre': name,
        'descripcion': description,
        'precio': price,
        'stock': stock,
        'categoria': category,
        'imagen': image if image != '' else 'https://via.placeholder.com/300x250?text=Sin+Imagen'
    }

    try:
        products.insert_one(nuevo_producto)
        # Redirige a la función listar para ver el catálogo actualizado
        return redirect(url_for('listar'))
    except Exception as e:
        return jsonify({'message': f'Error al guardar en la base de datos: {str(e)}'}), 500