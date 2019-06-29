# drfserialization

## installation

use python 3!

### create virtualenv
python -m venv .venv

### activate virtualenv
source .venv/bin/activate

### install requirements
pip install -r requirements.txt

### migrate
python manage.py migrate

### create superuser
python manage.py createsuperuser

### go to admin and create some students and addresses

### run dev server
python manage.py runserver

go to http://127.0.0.1:8000/student/list/ for serialization
go to http://127.0.0.1:8000/student/reverse_list/ for reversed serialization