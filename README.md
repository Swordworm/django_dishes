# Django Dishes
Installation:
1) git clone https://github.com/Swordworm/django_dishes.git
2) cd django_dishes
3) pip install virtualenv
4) virtualenv .venv
5) source .venv/bin/activate
6) pip install -r requirements.txt
7) sudo pacman -S postgresql or sudo apt-get install postgresql
8) sudo -u postgres psql postgres
9) create user admin with password '123';
10) alter role admin set client_encoding to 'utf8';
11) alter role admin set default_transaction_isolation to 'read committed';
12) alter role admin set timezone to 'UTC';
13) create database dishes_db owner admin;
14) \q
15) ./manage.py migrate
16) ./manage.py createsuperuser
17) admin
18) dev@gmail.com
19) 123
20) python3 manage.py runserver
21) Open your browser: http://127.0.0.1:8000/

Admin panel:
- username: admin
- password: 123
