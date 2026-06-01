# ProyectoBases
# 🎮 Tienda de Videojuegos  
Aplicación web desarrollada con **Python**, **Flask**, **MongoDB**, **HTML**, **Bootstrap** y **MongoDB Compass**.  
Permite gestionar productos de una tienda de videojuegos, incluyendo creación, listado, búsqueda y filtrado.

---

## 🚀 Características principales

### ✔ 1. Crear Producto  
Formulario para registrar nuevos videojuegos en la base de datos.  
Campos del formulario:

- **Nombre**
- **Descripción**
- **Precio**
- **Cantidad**
- **Imagen** (subida de archivo)

Los datos son guardados en MongoDB y se valida que estén completos.

---

### ✔ 2. Listar Productos  
Página que muestra **todos los videojuegos** registrados.

Funciones disponibles:
- Visualizar productos en tarjetas o tabla.
- **Editar** información de un producto.
- **Eliminar** un producto.

---

### ✔ 3. Buscar y Filtrar  
Permite encontrar productos usando diferentes criterios:

- **Por categoría**
- **Por nombre** (búsqueda con `regex`)
- **Por rango de precios** (mínimo y máximo)

La búsqueda es dinámica y combina todos los filtros.

---

## 🛠 Tecnologías utilizadas

- **Python 3**
- **Flask**
- **MongoDB** (local con MongoDB Compass)
- **HTML5**
- **Bootstrap 5**
- **Werkzeug**
- **Flask-PyMongo** o `pymongo`

---

## 📂 Estructura del proyecto

/project

│── app.py

│── database.py

│── product.py

│── filters.py

│── requirements.txt

│── /templates

│ ├── base.html

│ ├── crear.html

│ ├── listar.html

│ └── filtrosbusqueda.html

│── /static

│ └── uploads/ (imágenes de productos)

---
# Video   
El siguiente enlace es de un video mostrarndo como funciona esta aplicacion.
https://drive.google.com/file/d/1cLE2wNQ5weNgaHEPUILmIkCdbvIqmP_6/view?usp=sharing

---
