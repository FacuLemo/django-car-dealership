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
La única excepción a esto es la ruta de /user. En este caso para consultarla se debe estar logeado sí o sí, y para el resto de métodos se debe ser STAFF.

Las rutas que soporta la api son:

```python
localhost:8000/api/ #[GET] índice para la api.

localhost:8000/api/user/ #[GET,POST] Lista o crea un usuario usuarios.
localhost:8000/api/user/<id> #[GET,PATCH,PUT, DELETE] Muestra, edita o borra una usuario específico.
localhost:8000/api/user/<id>/toggle_lang/ #[POST] Post sin body, cambia el lenguaje de un usuario específico. Requiere ser STAFF.

localhost:8000/api/brand/ #[GET,POST] Lista o crea las marcas de autos.
localhost:8000/api/brand/<id> #[GET,PATCH,PUT, DELETE] Muestra, edita o borra una marca específica.

localhost:8000/api/category/ #[GET,POST]Lista o crea las categorías posibles para un auto.
localhost:8000/api/category/<id> #[GET,PATCH,PUT, DELETE] Muestra, edita o borra una categoría específica.

localhost:8000/api/car-status/ #[GET,POST]Lista o crea los estados posibles para un auto.
localhost:8000/api/car-status/<id> #[GET,PATCH,PUT, DELETE] Muestra, edita o borra un estado sespecífico.

localhost:8000/api/car-model/ #[GET,POST] Lista o crea los modelos de auto. Si es get anida la marca.
localhost:8000/api/car-model/<id> #[GET,PATCH,PUT, DELETE] Muestra, edita o borra un modelo de auto específico. Si es consulta, anida la marca.

localhost:8000/api/city/ #[GET] Lista las ciudades, anidadas. READ ONLY, incluso para staff.

localhost:8000/api/car/ #[GET,POST] Lista o crea publicaciones de autos. Si es get anida todo.
localhost:8000/api/car/<id> #[GET,PATCH,PUT, DELETE] Muestra, edita o borra un posteo de auto específico. Si es consulta, anida todo.
localhost:8000/api/car/<id>/comments #[GET] Muestra el auto consultado en un campo "car" y todos sus comentarios en un campo "comments". 

localhost:8000/api/comment/ #[POST, DELETE, PUT, PATCH] Permite agregar y borrar comentarios.
localhost:8000/api/user-bought-cars/ #[GET] Lista la tabla de relación entre usuarios y autos comprados, anidado. READ ONLY, incluso para staff.

```
Los endpoint retornan todos los campos de su respectivo modelo. Si son campos con claves foráneas, retornan el objeto anidado.
Al hacer post, también se deben enviar todos los campos del modelo (menos el id propio), y en los campos relacionales se debe enviar el ID correspondiente.
La única excepción a esto es User y los endpoint read only. Create examples más abajo.

Ejemplo de create user:
```json
{
  "username": "Matías",
  "email": "mati@mati.com",
  "is_staff": false,
  "password": "12345"
}
```
y al consultar user devuelve sólo los campos: `id, username y email`.

La ruta `city` y `user-bought-cars` son read only, sólo permiten el método GET.
City lista los campos `id, name, province y country`. donde province y country contienen un string con el nombre de la provincia/país correspondiente. User-bought-cars muestra todos los campos de su modelo.

Comment, por otro lado, sólo permite POST, DELETE, PUT y PATCH. Para consultar comentarios de debe hacer desde `car/id/comments`
Ejemplo de create comment:
```json
{
    "comment":"Este auto tenía mi tío, nunca lo dejó a pata. ¿Precio?",
    "car":11,
    "user":4
}
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
