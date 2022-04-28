# book-project-API 
 
## Steps : 
 
### 1 Install requirements 
pip install requirements.txt 
 
### 2 Run server 
python manage.py runserver 
 
### 3 Run Celery 
[linux OS] 
celery -A project worker --loglevel=info 
 
[Windows OS] 
celery -A project worker -l info --pool=solo 
 
### 4 Run celery-beat 
=============================== 
django-celery-beat 
=============================== 
 
celery -A project beat -l INFO  # For deeper logs use DEBUG 
celery -A project worker -B -l INFO 
 
