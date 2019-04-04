#Installar pip y venv
1. `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
2. `python3 get-pip.py`
3. `pip install virtualenv`

# Crear proyecto de DJANGO
1. Crear una carpeta project_name
2. Dentro de la carpeta ejecutar `virtualenv --python=python3 venv`
3. Activar el venv con `source venv/bin/activate`
4. Desctivar con `deactivate`
6. Instalar los requerimientos del env `pip install -r requirements.txt`
7. Create a folder `mkdir src`
8. Dentro de src `django-admin.py startproject project_name`
9. Dentro de `src/project_name`, correr el comando `python manage.py startapp prject_name_api`
