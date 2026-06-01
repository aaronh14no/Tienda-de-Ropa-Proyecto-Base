from flask import Blueprint, redirect, url_for
import database as dbase

db = dbase.dbConnection()
eliminar_producto_bp = Blueprint('eliminar_producto_bp', __name__)

@eliminar_producto_bp.route('/delete/<product_name>')
def delete(product_name):
    # Usamos la colección 'products'
    products = db['products']
    
    # Intentamos eliminar por 'nombre' (español) o 'name' (inglés)
    # Lo ideal es que sea el mismo campo que usas en el listar
    products.delete_one({'$or': [
        {'nombre': product_name},
        {'name': product_name}
    ]})
    
    return redirect(url_for('listar'))