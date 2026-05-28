from flask import Blueprint, render_template, redirect, url_for
import database as dbase
from bson.objectid import ObjectId

db = dbase.dbConnection()

eliminar_producto_bp = Blueprint('eliminar_producto_bp', __name__)

@eliminar_producto_bp.route('/products/<string:product_id>/delete', methods=['GET'])
def confirmar_eliminacion(product_id):
    products = db['products']
    product = products.find_one({'_id': ObjectId(product_id)})
    return render_template('confirmar_eliminacion.html', product=product)

@eliminar_producto_bp.route('/products/<string:product_id>/delete', methods=['POST'])
def eliminar(product_id):
    products = db['products']
    products.delete_one({'_id': ObjectId(product_id)})
    return redirect(url_for('buscar_filtrar_bp.buscar_y_filtrar'))