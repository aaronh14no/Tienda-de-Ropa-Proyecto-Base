from flask import Blueprint, render_template, request, redirect, url_for
import database as dbase

products = dbase.dbConnection()['products']

editar_producto_bp = Blueprint('editar_producto_bp', __name__)

@editar_producto_bp.route('/edit/<string:product_name>', methods=['GET', 'POST'])
def edit(product_name):
    # guardar cambios (POST)
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        stock = request.form.get('stock')
        category = request.form.get('category')

        products.update_one(
            {'name': product_name},
            {'$set': {
                'name': name,
                'description': description,
                'price': price,
                'stock': stock,
                'category': category
            }}
        )
        return redirect(url_for('listar'))
    
    # mostrar formulario (GET)
    product = products.find_one({'name': product_name})
    return render_template('edit.html', product=product)



