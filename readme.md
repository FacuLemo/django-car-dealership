### Car Dealership Management System University project made by:
- [Facundo Lemo](https://github.com/FacuLemo)
- [Luca Petrocchi](https://github.com/lucapetrocchi)

# Set up
1. create virtual environment:
```bash
  python3 -m venv venv
```
2. activate the venv:
```bash
  source venv/bin/activate
```
3. Install requirements:
```bash
  pip install -r requirements.txt
```
4. run migrations:
```bash
  python3 manage.py migrate
```
5. Run Django project:
```bash
  python3 manage.py runserver
```

/home <- lista de todos los autos, filter by status
/profile/:account <- usuario & todos sus autos
/car (list & create & update) [list es privado, create & update es acceso parcial a autor + staff] :check:
/category (list & create & update) [privados (para staff y admin)] :check:
/brand (list & create & update) [privados (para staff y admin)] :check:
/roles (list & create & update) [privados (para staff y admin)] :check:
