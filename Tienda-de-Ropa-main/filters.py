# filters.py
from flask import request

def build_filter_query():
    """
    Construye el diccionario de consulta de MongoDB a partir de los 
    parámetros de la URL. Adaptado para llaves en español.
    """
    
    # 1. Obtenemos los parámetros que viajan en la URL desde el formulario HTML
    category = request.args.get('category')
    name_search = request.args.get('name')
    min_price_str = request.args.get('min_price')
    max_price_str = request.args.get('max_price')

    query = {}

    # 2. Aplicar Filtro por Categoría
    # CORRECCIÓN: Cambiamos 'category' por 'categoria' que es el nombre real en tu base de datos
    if category: 
        query['categoria'] = category

    # 3. Aplicar Búsqueda por Nombre (utilizando $regex)
    # CORRECCIÓN: Cambiamos 'name' por 'nombre'
    if name_search:
        # La 'i' hace la búsqueda insensible a mayúsculas/minúsculas. 
        # Al usar $regex, encontrará "tennis" aunque en la base de datos se llame "zapatos_tennis".
        query['nombre'] = {'$regex': name_search, '$options': 'i'}

    # 4. Aplicar Filtro por Rango de Precio
    price_range = {}
    
    # Manejo de precio mínimo
    if min_price_str:
        try:
            price_range['$gte'] = float(min_price_str)
        except ValueError:
            pass
    
    # Manejo de precio máximo
    if max_price_str:
        try:
            price_range['$lte'] = float(max_price_str)
        except ValueError:
            pass

    # 5. Si hay condiciones de precio, se añaden a la query principal
    # CORRECCIÓN: Cambiamos "$price" por "$precio" para que convierta el campo correcto a Double
    if price_range:
        expr = []
        if '$gte' in price_range:
            expr.append({
                '$gte': [ { '$toDouble': "$precio" }, price_range['$gte'] ]
            })

        if '$lte' in price_range:
            expr.append({
                '$lte': [ { '$toDouble': "$precio" }, price_range['$lte'] ]
            })

        query['$expr'] = expr[0] if len(expr) == 1 else { '$and': expr }
        
    # Devuelve el diccionario de consulta listo para productos.find(query)
    return query