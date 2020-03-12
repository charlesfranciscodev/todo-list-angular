# TODO List

Your task is to create the web frontend of a todo list app.
Preferably, you should use a frontend framework (Angular, React or Vue).
The backend is already done for you (see API documentation below).

## Features

### Home Page

#### Done
* View a dashboard with all the todos.
* Create a new todo item.
* Delete a todo item.

#### TODO
* Update a todo item by clicking on it and opening up a modal.
* Filter todos by title, completion or username.
* Sort todos by title, due date or priority.

### Users Page

#### TODO
* View an image gallery of all users.

## API Routes

### Todos

* **GET** `/api/todos`
* **GET** `/api/todos/{:id}`
* **PUT** `/api/todos`
* **DELETE** `/api/todos/{:id}`

### Users

* **GET** `/api/users`
* **GET** `/api/users/{:id}`

## Dependencies
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

## Frontend Setup (from scratch)
```
npm install -g @angular/cli
ng new client
```

## Development Workflow

### Build the images

`docker-compose build`

### Run the containers

`docker-compose up`

The API should be accessible at [http://localhost:5000](http://localhost:5000).

### Create the database

`docker-compose exec server python manage.py recreate_db`

### Seed the database

`docker-compose exec server python manage.py seed_db`

### Postgres

Want to access the database via psql?

```
docker-compose exec database psql -U postgres
\connect db_dev
```

### Connect to the server

`docker-compose exec server /bin/sh`

### Create a new component
`ng generate component components/example`

### Create a new service
`ng generate service services/example`

## References
* [testdriven.io](https://testdriven.io)
* [Flask](https://palletsprojects.com/p/flask/)

## Data
* [Random User Generator](https://randomuser.me/)
* [Diverse UI](https://diverseui.com/)
