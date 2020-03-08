# TODO List

Your task is to create the web frontend of a todo list app.
Preferably, you should use a frontend framework (preferably Angular, React or Vue).
The backend is already done for you (see API documentation below).

## Features

### Home Page
* View a dashboard with all the todos.
  * Filter todos by title, completion or username.
  * Sort todos by title, due date or priority.
* Create a new todo item.
* Update a todo item by clicking on it and opening up a modal.
* Delete a todo item.

### Users Page
* View an image gallery of all users.

## API Routes

### Todos

**GET** `/api/todos`

Response
```json
[
  {
    "completed": false,
    "content": "Pudding sweet roll bear...",
    "dueDate": "2020-04-30",
    "priority": 2,
    "title": "Pudding",
    "todoId": 1,
    "user": {
      "avatarUrl": "https://charlesfranciscodev.github.io/images/diverseui/male-52.jpg",
      "firstName": "Richard",
      "lastName": "Burke",
      "userId": 4,
      "username": "whiteostrich"
    }
  },
  {
    "completed": false,
    "content": "Sesame snaps gummi bears...",
    "dueDate": "2020-01-02",
    "priority": 1,
    "title": "Sesame snaps",
    "todoId": 2,
    "user": {
      "avatarUrl": "https://charlesfranciscodev.github.io/images/diverseui/male-30.jpg",
      "firstName": "Dominic",
      "lastName": "Margaret",
      "userId": 1,
      "username": "lazybear"
    }
  }
]
```

---

**GET** `/api/todos/{:id}`

Response

```json
{
  "completed": true,
  "content": "Chocolate cake bear claw...",
  "dueDate": "2020-12-29",
  "priority": 2,
  "title": "Muffin",
  "todoId": 4,
  "user": {
    "avatarUrl": "https://charlesfranciscodev.github.io/images/diverseui/female-11.jpg",
    "firstName": "Laura",
    "lastName": "Petersen",
    "userId": 8,
    "username": "blackelephant"
  }
}
```

---

**POST** `/api/todos`

Request
```json
{
  "title": "My Title",
  "content": "Ice cream apple pie...",
  "completed": true,
  "dueDate": "2020-05-30",
  "priority": 3,
  "user_id": 12
}
```

Response
```json
{
  "message": "Todo created successfully",
  "todo_id": 17
}
```

---

**PUT** `/api/todos`

Request
```json
{
  "todo_id": 13,
  "title": "My Title",
  "content": "This is the content",
  "completed": false,
  "dueDate": "2019-05-30",
  "priority": 1,
  "user_id": null
}
```

Response
```json
{
  "message": "Todo updated successfully",
  "todo_id": 13
}
```

---

**DELETE** `/api/todos/{:id}`

Response

204 | when the todo is successfully deleted

404 | when the todo is not found

### Users

**GET** `/api/users`

Response
```json
[
  {
    "avatarUrl": "https://charlesfranciscodev.github.io/images/diverseui/male-30.jpg",
    "firstName": "Dominic",
    "lastName": "Margaret",
    "userId": 1,
    "username": "lazybear"
  },
  {
    "avatarUrl": "https://charlesfranciscodev.github.io/images/diverseui/female-69.jpg",
    "firstName": "Antonietta",
    "lastName": "Sanchez",
    "userId": 2,
    "username": "orangekoala"
  }
]
```

---

**GET** `/api/users/{:id}`

Response
```json
{
  "avatarUrl": "https://charlesfranciscodev.github.io/images/diverseui/male-30.jpg",
  "firstName": "Dominic",
  "lastName": "Margaret",
  "userId": 1,
  "username": "lazybear"
}
```

### Test

**GET** `/api/test`

Response
```json
{
  "message": "Yo mamma so fat even penguins are jealous of the way she waddles."
}
```

## Dependencies
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

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

## References
* [testdriven.io](https://testdriven.io)
* [Flask](https://palletsprojects.com/p/flask/)

## Data
* [Random User Generator](https://randomuser.me/)
* [Diverse UI](https://diverseui.com/)
