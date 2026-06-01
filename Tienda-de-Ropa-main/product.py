class Product:
    def __init__(self, name, description, price, stock, category, image):
        self.name = name
        self.description = description
        
      
        self.price = float(price) if price else 0.0
        self.stock = int(stock) if stock else 0
        
        self.category = category
        self.image = image

    def toDBCollection(self):
        return {
            "nombre": self.name,
            "descripcion": self.description,
            "precio": self.price,   # Ahora se guardará de color morado en Compass (Número)
            "stock": self.stock,
            "categoria": self.category,
            "imagen": self.image
        }