# isen-fr2i-2019

## Prérequis

- SGBDR fonctionnel (par exemple PostgreSQL ou MariaDB)
- Python et pipenv installés

## Base de données

- Créer une base de données à utiliser dans le projet. Par exemple pour MariaDB:
`CREATE DATABASE db_name;`
- Créer un utilisateur. Par exemple pour MariaDB:
`CREATE USER 'username@'locahost' IDENTIFIED BY 'password';`
- Donner toutes les permissions pour la base de données à l'utilisateur. Par exemple pour MariaDB:
`GRANT ALL PRIVILEGES ON db_name.* TO 'username'@'localhost';`

## Pipenv

- Créer un environnement virtuel depuis le dossier du projet:
`pipenv install`
- Accéder à cet environnement:
`pipenv shell`

## Paramètres locaux

- Dans le dossier `ynquiz_website`, créer `local_settings.py` et remplir les informations nécessaires pour se connecter à la base de données. Example utilisant MariaDB:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ynquiz_mariadb',
        'USER': 'antoine',
        'PASSWORD': 'azerty',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

## Premier lancement

- Avant le premier lancement, dans le dossier `ynquiz_website`, effectuer les migrations: `python manage.py makemigrations quiz` puis `python manage.py migrate`
- Pour lancer l'application : `python manage.py runserver`