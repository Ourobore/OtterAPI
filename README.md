# OtterAPI
A small API to learn Python Django.
<br/>
<br/>

## How to run the app
First, create a Python virtual environment and activate it:
``` bash
$ python3 -m venv .env
$ source .env/bin/activate
```

Then, install the app requirements int the virtual environment with `pip`:
``` bash
$ pip3 install -r requirements.txt
```

Finally, create the `.env` and start the Django server in a virtual environment with the setup variables exported (see `Environment variables` field below for more info):

``` bash
$ env $(cat .env) python3 manage.py runserver
```
<br/>

## Environment variables
The following envrionment variables are needed in a `.env` file to setup the Django server and PostgreSQL database. Replace their values with yours.

```
DJANGO_SECRET_KEY=my_super_secret_and_long_secret_key
PSQL_NAME=database
PSQL_USER=my_psql_user
PSQL_PASSWORD=my_psql_password
PSQL_HOST=my_psql_host
PSQL_PORT=my_psql_host
```
