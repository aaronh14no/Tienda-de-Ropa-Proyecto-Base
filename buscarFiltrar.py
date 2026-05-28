from flask import Blueprint, request, render_template, current_app
import database as dbase

# Conectamos a la misma base de datos
db = dbase.dbConnection()

buscar_filtrar_bp = Blueprint('buscar_filtrar_bp', __name__)

@buscar_filtrar_bp.route('/products/search', methods=['GET'])
def buscar_y_filtrar():
    # 1. Obtener los parámetros que envía el usuario desde el frontend
    query_nombre = request.args.get('query', '').strip()
    categoria = request.args.get('category', '').strip()
    min_price = request.args.get('min_price', '').strip()
    max_price = request.args.get('max_price', '').strip()
    # 2.  filtro dinámico para MongoDB
    filtros = {}
    # HU-05: Búsqueda por nombre 
    if query_nombre:
        filtros['name'] = {'$regex': query_nombre, '$options': 'i'}

    # HU-06: Filtro por categoría
    if categoria and categoria != "Todas":
        filtros['category'] = categoria
        

    #3. 08 FILTRO PRECIO

    if min_price or max_price:
    
        filtros['price'] = {}
    
        try:
    
            if min_price != '':
                filtros['price']['$gte'] = float(min_price)
    
            if max_price != '':
                filtros['price']['$lte'] = float(max_price)
    
        except ValueError:
    
            return "Precio inválido", 400
    collection = db['products']
    productos_encontrados = list(collection.find(filtros))
    # Pasamos los resultados a la plantilla para que se rendericen en tarjetas
    return render_template('listar.html', productos=productos_encontrados, query=query_nombre, category_selected=categoria)
 