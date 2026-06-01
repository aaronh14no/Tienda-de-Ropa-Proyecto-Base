from flask import Blueprint, redirect, jsonify
import database as dbase

db = dbase.dbConnection()

eliminar_producto_bp = Blueprint('eliminar_producto_bp', __name__)

@eliminar_producto_bp.route('/delete/<string:product_name>', methods=['GET'])
def delete(product_name):
    products = db['products']
    try:
        # Borramos en Mongo
        products.delete_one({'nombre': product_name})
        
        # 🌟 Cambiamos url_for por la ruta de texto directo para evitar el Not Found
        return redirect('/listar')
        
    except Exception as e:
        return jsonify({'message': f'Error al eliminar: {str(e)}'}), 500