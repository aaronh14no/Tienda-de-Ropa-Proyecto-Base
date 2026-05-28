from flask import Blueprint, request, jsonify, redirect, url_for, current_app, flash
from product import Product
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
    name = request.form['name']
    description = request.form['description']
    price = float(request.form['price'])
    stock = int(request.form['stock'])
    category = request.form['category']

    image = ''

    if 'image' in request.files:
        file = request.files['image']
        if file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(current_app.config['UPLOAD_FOLDER2'], filename)
            file.save(save_path)
            image = filename

    if name and description and price and stock and category:
        product = Product(name, description, price, stock, category, image)
        try:

            stock = int(request.form['stock'])
        
            if stock < 0:
                return jsonify({
                    'message': 'El stock no puede ser negativo'
                }), 400
        
        except ValueError:
        
            return jsonify({
                'message': 'El stock debe ser numérico'
            }), 400
        try:
        
            price = float(request.form['price'])
        
        except ValueError:
        
            return jsonify({
                'message': 'El precio debe ser numérico'
            }), 400
        if not name or not description or not category:
            return jsonify({
                'message': 'Campos incompletos'
            }), 400
        products.insert_one(product.toDBCollection())
        flash("Producto creado correctamente.", "success")
        return redirect(url_for('home'))

    flash("No se pudo crear el producto. Completa todos los campos.", "danger")
    return redirect(url_for('home'))