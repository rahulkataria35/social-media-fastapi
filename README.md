
# Complete Back-end repository of social media app by using Python's FastAPI framework.



### Project Structure:

- `app:` Contains the core application logic, including models, routes, utilities, and database interactions.
- `alembic:` Houses the Alembic migration scripts for database schema changes.
- `docker-compose-dev.yml` & `docker-compose-prod.yml`: Define configurations for development and production environments using Docker Compose.
- `Dockerfile`: Instructions for building the Docker image for the application.
- `entrypoint.sh`: Script executed at container startup (optional).
- `requirements.txt`: Lists all Python dependencies required for the project.
- `tests`: Contains unit tests for different parts of the application.
- `README.md` (You are here!): Provides an overview of the project.

### Getting Started:

- `Prerequisites`: Ensure you have Python (version 3.x recommended) and Docker installed on your system.

### Install Dependencies:

- Navigate to the project directory.
- Run `pip install -r requirements.txt` to install the required libraries.

`Development Environment:`

To Run the application for local environment:
- `sh local_env_up.sh`

To see our application is running or not:
- `docker ps`

To stop the application:

- `sh local_env_down.sh`

Access the application: The application will be accessible by default at http://0.0.0.0:8000 , you should see:
```

{
    "status": "up"
}

```

Then you can use following link to use the  API

````
http://0.0.0.0:8000/docs 

````

#### This API  has 4 routes

## 1) Post route

#### This route is reponsible for creating post, deleting post, updating post and Checkinh post

## 2) Users route

#### This route is about creating users and searching user by id

## 3) Auth route

#### This route is about login system

## 4) Vote route

 #### This route is about likes or vote system and this route contain code for upvote or back vote there is not logic about down vote




# Production Environment:

Configure your production environment details (database credentials, secrets, etc.) in docker-compose-prod.yml.
Use `prod_env_up.sh` to run the application in production mode.


# how to run locally without Docker

First clone this repo by using following command

````

git clone <repo_url>

````
then 
````

cd backend_social_media_app

````

Then create Virtual environment according to your OS and activate it. and then install the requirements.txt using 

````

pip3 install -r requirements.txt

````

- create a .env file and add Environment variables to connect Database:
````
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=passward_that_you_set
DATABASE_NAME=name_of_database
DATABASE_USERNAME=User_name
SECRET_KEY=09d25e094faa2556c818166b7a99f6f0f4c3b88e8d3e71234567898765432 
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30 

````


Then go to ./app folder using `cd ./app` and then run 

````
alembic upgrade head

````


Then run
````

python3 main.py

````
Once the file run, navigate to http://localhost:8000/. You should see:

```

{
    "status": "up"
}

```


Then you can use following link to use the  API

````
http://127.0.0.1:8000/docs 

````

## Testing:

The project includes unit tests in the tests directory. You can run them using a test runner like pytest.

## Additional Information:

The `alembic.ini`file configures Alembic for database migrations.
The `.env` files (not included in this repository for security reasons) store environment-specific variables like database credentials and secret keys.

### Contributing:

Pull requests and bug reports are welcome.
