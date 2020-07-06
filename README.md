# Notes App

Notes App is a full-stack project made with Vue.js in the client and Django/DRF in the backend.
It's a CRUD API for notes and a client that shows the notes and let you create more.

## Installation

For the API, create a virtual enviroment and pip install the requirements.

```bash
cd api/
virtualenv —python=python3 venv
source venv/bin/activate
cd crud/
pip install -r requirements.txt

```

For the client install Vue and Bootstrap-Vue
```bash
npm install
npm install vue bootstrap-vue bootstrap
```

## Usage

### Django server:
In crud/ directory, make the migrations and run the server
```bash
python manage.py migrate
python manage.py runserver
```
Endpoints are:
* admin/ - Django Admin

* api/notes/ - List Notes
* api/notes/create - Create Note
* api/notes/{id}/ - Update and Retrieve Note
* api/notes/delete - Delete Note

* api/users/ - List and Create Users,
* api/users/{id} - Update and Delete Users

### Vue client
In notes-app/ directory, run npm server
```bash
npm run serve
```

## License
[MIT](https://choosealicense.com/licenses/mit/)