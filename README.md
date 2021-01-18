# FlaskPostgresDocker

Running Flask and postgres with docker-compose. Save to db using forms, display saved entries from db


# Run
Start and build container
```
 docker-compose up -d --build
```
Create new db instance
```
 docker-compose exec web python manage.py create_db
```



# Other helful commands used while learning

### Virtual environment


To run commands in powershell
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Create virtual environment
```
py -3 -m venv venv
```
Activate
```
.venv/Scripts/Activate.ps1
```

### Set environment variables(Windows) for flask

```
 $env:FLASK_APP = "/app"          
 $env:FLASK_ENV = "development"
```

### Install psycopg2-binary


```
python -m pip install psycopg2-binary
```

### Connect to postgres db in container


```
docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev
\c hello_flask_dev    # Connect to db
\dt                   # List all tables
select * from users;  # Display all users
\q                    # Quit
```
