from flask import Blueprint, render_template, request, redirect, url_for, flash
import database as dbase
from bson.objectid import ObjectId

db = dbase.dbConnection()

editar_producto_bp = Blueprint('editar_producto_bp', __name__)

@editar_producto_bp.route('/products/<string:product_id>/edit', methods=['GET', 'POST'])
def edit(product_id):
    products = db['products']

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        stock = request.form.get('stock')
        category = request.form.get('category')

        if int(stock) < 0:
            flash("El stock no puede ser negativo.", "danger")
            return redirect(url_for('buscar_filtrar_bp.buscar_y_filtrar'))

        if float(price) <= 0:
            flash("El precio debe ser mayor a 0.", "danger")
            return redirect(url_for('buscar_filtrar_bp.buscar_y_filtrar'))

        products.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': {
                'name': name,
                'description': description,
                'price': float(price),
                'stock': int(stock),
                'category': category
            }}
        )
        flash("Producto actualizado correctamente.", "success")
        return redirect(url_for('buscar_filtrar_bp.buscar_y_filtrar'))

    product = products.find_one({'_id': ObjectId(product_id)})
    return render_template('edit.html', product=product)