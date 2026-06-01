from flask import Blueprint, render_template, request, redirect, url_for
import database as dbase

db = dbase.dbConnection()

editar_producto_bp = Blueprint('editar_producto_bp', __name__)

@editar_producto_bp.route('/edit/<string:product_name>', methods=['GET', 'POST'])
def edit(product_name):
    products = db['products']

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        stock = request.form.get('stock')
        category = request.form.get('category')

        products.update_one(
            {'name': product_name},
            {'$set': {
                'nombre': name,
                'descripcion': description,
                'precio': price,
                'stock': stock,
                'categoria': category
            }}
        )
        return redirect(url_for('listar'))

    product = products.find_one({'nombre': product_name})
    return render_template('edit.html', product=product)