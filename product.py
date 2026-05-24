class Product:
    def __init__(self, name, description, price, stock, category, image=''):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.image = image

    def toDBCollection(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'category': self.category,
            'image': self.image
        }