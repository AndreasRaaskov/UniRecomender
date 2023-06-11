# usage
The database keeps track of reviews made by users of universities they attended as per the ER diagram. It uses cascade to remove relations when entities (users etc.) are deleted. We intended to update universities average ratings inside the database, but did not get this far due to issues with the webapp.

## Requirements:
Run the code below to install the necessary modules.

>$ pip install -r requirements.txt

## Database init
1. set the database in __init__.py file.
2. run schema.sql, schema_ins.sql, schema_upd.sql, schema_upd_2.sql in your database.

## Running flask
### The python way

$ python3 run.py

### The flask way.

$ export FLASK_APP=run.py

$ export FLASK_DEBUG=1           (Replaces export FLASK_ENV=development)

$ export FLASK_RUN_PORT=5004     (Optional if you want to change port numbe4. Default port is port 5000.)

$ flask run


For Windows you may have to use the SET command instead of EXPORT. Ex set FLASK_APP=run.py; set FLASK_DEBUG=1; flask run. This worked for me. Also remeber to add the path to your postgres bin-directory in order to run (SQL interpreter) and other postgres programs in any shell.


### The flask way with a virual environment.

Set up virtual environment as specified in https://flask.palletsprojects.com/en/1.1.x/installation/ (OSX/WINDOWS)

OSX:

Create virtual environment in folder

$ mkdir myproject

$ cd myproject

$ python3 -m venv .venv

Activate virtual environment in folder

$ . .venv/bin/activate

Install flask

$ pip install Flask



Set environment variables and start flask

$ export FLASK_APP=run.py

$ export FLASK_DEBUG=1           (Replaces export FLASK_ENV=development)

$ export FLASK_RUN_PORT=5000     (Optional if you want to change port number. Default port is port 5000.)

$ flask run