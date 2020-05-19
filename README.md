# Bus Databse

Purpose: To use more of flask's database features. 

Reference to this: https://cs50.harvard.edu/web/2018/notes/4/


Step 1: create database in postgres
```
CREATE DATABASE buses
```
only real command that needs to be run in postgres

Step 2: make sure environment variables are properly specified. I use a file called ```env.sh``` which contains two important variables. It is good practice not to add environment files to your github, which is why env.sh is not here. env.sh contains
```
DATABASE_URI="postgres+psycopg2:///buses"
FLASK_APP="application.py"
```
In which the database URI being refernced in ```create.py``` and ```application.py``` and the flask app variable being necessary to run flask. 
Make sure to source this with:
```
source env.sh
```
or export the variables manually:
```
export DATABASE_URI="postgres+psycopg2:///buses"
export FLASK_APP="application.py"
```

Step 3: Setup Python
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

Step 4: Setup Tables
Tables can be setup with ```config.py``` which will use the variables specified in ```models.py```
Run with:
```
python config.py
```

