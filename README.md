# Bus Databse

This Flask project displays a table of buses from Singapore to KL generated from two database tables.

The purpose of this project is to expand on my [Airline Project](https://github.com/asteinig4018/sql_dev) by using Flask and SQLAlchemy's ORM features instead of generating SQL for the database, largely learned from here: https://cs50.harvard.edu/web/2018/notes/4/

## Technologies Used

* Flask 1.1.2
* Python 3.6
* Postgres 10.12
* SQLAlchemy 1.3
* Jinja 2.11
* Bootstrap 

## Use

### Setup

#### Step 1: Create the Database in Postgres
This is the only real command that needs to be run in postgres
```
CREATE DATABASE buses
```


#### Step 2: Setup the Environment
This step is to make sure environment variables are properly specified. I use a file called ```env.sh``` which contains two important variables. It is good practice not to add environment files to your repositories, which is why my ```env.sh``` is not here. My ```env.sh``` contains:
```
DATABASE_URI="postgres+psycopg2:///buses"
FLASK_APP="application.py"
FLASK_DEBUG=1
```
In which the database URI being refernced in ```create.py``` and ```application.py``` and the flask app variable being necessary to run flask. I also specificy flask should run in debug mode, but this is not necessary. 
Make sure to source this with:
```
source env.sh
```
or export the variables manually:
```
export DATABASE_URI="postgres+psycopg2:///buses"
export FLASK_APP="application.py"
```

Note: the URI I have specified only works because the database is hosted locally and I am a root user.

#### Step 3: Setup Python
I suggest using a virtualenv by executing
```
pip install virtualenv
python -m venv env
```
If your terminal prompt does not show anything such as 'e' or something to show you are in the virtual environment, you can activate it by running
```
source /env/bin/activate.sh
```
Now install the required packages by running
```
pip install -r requirements.txt
```

#### Step 4: Setup Tables
Tables can be setup with ```config.py``` which will use the variables specified in ```models.py```.
Run with:
```
python config.py
```

### Run

```
flask run
```

## Data
The sample data from the csv files is inspired from actual buses lines that I used but are not real data. 
