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