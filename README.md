# Note Management System
# Requirement
* django>=3.2
* python>=3.9
* docker (Optional)

# Clone Project 
```
git clone https://github.com/chitthushine/note-management.git
```

# Local Setup
* Create Virtual Environment and install requirements (First Time Only)
```
cd note-management
python3 -m venv env
source env/bin/activate
pip install -r django/requirements.txt
```

* Database Setup (First Time Only)
```
cd django
python manage.py migrate
```

* Run Unit Test
```
cd django
python manage.py test apps.note.tests
```

* Create superuser to access admin page (optional) (First Time Only)
```
cd django
python manage.py setupuser
```

* Run Django
```
cd django
python manage.py runserver
```

# Running with Docker

* Up Django Container
```
docker compose up -d
```

* Database Setup (First Time Only)
```
docker exec -u root -it "$(docker-compose ps -q django)" python manage.py migrate
```

* Run Unit Test
```
docker exec -u root -it "$(docker-compose ps -q django)" python manage.py test apps.note.tests
```

* Create superuser to access admin page (optional) (First Time Only)
```
docker exec -u root -it "$(docker-compose ps -q django)" python manage.py setupuser
```

# Accounts

* default url 
  * site : `http://localhost:8000` or `http://127.0.0.1:8000`
  * for admin page, 
    - username: `admin`
    - password: `bh>R4!S]`
