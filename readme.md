# Índice
- [Proyecto](#proyecto)
- [Web App](#web-app)
- [Api Rest](#api-rest)
- [Setup](#set-up)
- [Diseño de base de datos](#diseño-de-base-de-datos)
- [Imágenes del proyecto](#imágenes)

# Proyecto
Foro de compra-venta de autos nuevos/usados. Está desarrollado en Django, y forma parte del trabajo final integrador de la materia Ingeniería de software del iTEC.

Realizado por
- [Facundo Lemo](https://github.com/FacuLemo)
- [Luca Petrocchi](https://github.com/lucapetrocchi)

Profesor a cargo
- [Matías Lucero](https://github.com/matiasjavierlucero/)


# Web App
Tiene funcionalidades CRUD disponibles para el staff y superusers para marcas de autos, categorías, y roles cosméticos. Estas no son accessibles para usuarios comunes.

Cada usuario puede publicar autos para venta, y otros pueden comentar en el post de venta. Al efectuar una compra, el auto se marca como vendido y comienza a aparecer en el perfil del comprador. 

Los autos pueden filtrarse por estatus, modelo, y marca.

Las rutas disponibles para el staff son:

```
cars/ brand/ (GET)
cars/ brand/create (GET y POST)
cars/ brand/<int:id> (GET y POST)
cars/ brand/delete/<int:id> (POST)
cars/ category/ (GET)
cars/ category/create (GET y POST)
cars/ category/<int:id> (GET y POST)
cars/ category/delete/<int:id> (POST)
cars/ car_status/ (GET)
cars/ car_status/create (GET y POST)
cars/ car_status/<int:id> (GET y POST)
cars/ car_status/delete/<int:id> (POST)
cars/ car_model/ (GET)
cars/ car_model/create (GET y POST)
cars/ car_model/<int:id> (GET y POST)
cars/ car_model/delete/<int:id> (POST)

users/ role/ (GET)
users/ role/create (GET y POST)
users/ role/<int:id> (GET y POST)
users/ role/delete/<int:id> (POST)
users/ user_role/ (GET)
users/ user_role/create (GET y POST)
users/ user_role/<int:id> (GET y POST)
users/ user_role/delete/<int:id> (POST)


```

Las rutas de usuario son:

```
login/ (GET y POST)
logout/ (POST)
register/ (GET y POST)

cars/ (GET y POST) [listado de autos]
cars/ <int:id> (GET y POST) [detalle]
cars/ sell/ (GET y POST) [para hacer venta de auto]
cars/ update-sale/<int:id> (GET y POST)
cars/ delete-sale/<int:id> (POST)
cars/ create-comment/ (POST) [aparece en el detalle de un auto]
cars/ delete-comment/<int:id> (POST) [ditto]
cars/ make-sale/<int:id> (POST) [usada al comprar un auto a la venta]

users/ <int:id> (GET) [perfil]

```

# Api Rest
Adicionalmente a la navegación web, este proyecto también es operable a través de una API REST, desarrollada con Django-Rest-Framework

Se puede consultar (método GET) a cualquier ruta sin estar logeado. Sin embargo, para cualquier otro método se debe ser un usuario STAFF, autenticado a través del basic-auth que otorgan los clientes de api-rest como postman o thunderclient.

Las rutas que soporta la api son:

```
localhost:8000/api/ #índice para la api.

localhost:8000/api/brand/ #Lista las marcas de autos.
localhost:8000/api/brand/<id> #Muestra una marca específica.

localhost:8000/api/category/ #Lista las categorías posibles para un auto.
localhost:8000/api/category/<id> #Muestra una categoría específica.

localhost:8000/api/car-status/ #Lista los estados posibles para un auto.
localhost:8000/api/car-status/<id> #Muestra un estado sespecífico.

localhost:8000/api/car-model/ #Lista los modelos de auto, anida la marca.
localhost:8000/api/car-model/<id> #Muestra un modelo de auto específico, anida la marca.

localhost:8000/api/city/ #Lista las ciudades, anidadas. READ ONLY, incluso para staff.
```


# Set up
1. Crear entorno virtual:
```bash
  python3 -m venv venv
```
2. Activarlo:
```bash
  source venv/bin/activate
```
3. Instalar dependencias:
```bash
  pip install -r requirements.txt
```
4. Migrar base de datos:
```bash
  python3 manage.py migrate
```
5. Iniciar proyecto:
```bash
  python3 manage.py runserver
```

# Diseño de Base de Datos

![readme9](/readme_images/readme9.png)

# Imágenes

![readme1](/readme_images/readme1.png)
![readme2](/readme_images/readme2.png)
![readme2](/readme_images/readme2.png)
![readme3](/readme_images/readme3.png)
![readme4](/readme_images/readme4.png)
![readme5](/readme_images/readme5.png)
![readme6](/readme_images/readme6.png)
![readme8](/readme_images/readme8.png)
