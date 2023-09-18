# Flask Application for CRUD Operations on MongoDB

This Flask application provides REST API endpoints for CRUD (Create, Read, Update, Delete) operations on a User resource using a MongoDB database. It allows you to manage user data with the following fields:

- id (a unique identifier for the user)
- name
- email
- password

The application is containerized using Docker for easy setup.

## Prerequisites

- Docker
- Python 3.9 or higher
- Virtual Environment

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rkvishnu/flask-mongodb-users.git
   cd flask-mongodb-crud
   ```

Create and activate a virtual environment:

```bash
 
python -m venv venv
source venv/bin/activate
Install Python dependencies:
```

```bash
pip install -r requirements.txt
```

# Running the Application

Start the Docker containers (Flask app and MongoDB):

```
docker-compose up --build
```

- The Flask app should be accessible at http://localhost:5000

# API Documentation
- Create a New User
URL: http:localhost:5000/users
Method: POST
Request Body:

json
{
"name": "John Doe",
"email": "johndoe@example.com",
"password": "securepassword"
}
Response:

json
{
"user_id": "user_id_here"
}

- Get All Users
URL: /users

Method: GET

Response:

json
Copy code
{
"users": [
{
"id": "user_id_here",
"name": "John Doe",
"email": "johndoe@example.com"
},
{
"id": "user_id_here",
"name": "Alice Smith",
"email": "alicesmith@example.com"
},
...
]
}

- Get User by ID
URL: /users/<user_id>
Method: GET
Response:

json
Copy code
{
"id": "user_id_here",
"name": "John Doe",
"email": "johndoe@example.com"
}


- Update User by ID
URL: /users/<user_id>
Method: PUT
Request Body:

json
{
"name": "Updated Name",
"email": "updatedemail@example.com"
}
Response:

json
{
"message": "User updated successfully"
}


- Delete User by ID : 

URL: /users/<user_id>
Method: DELETE
Response:

json
{
"message": "User deleted successfully"
}


# stop the application
Stopping the Application
To stop the Docker containers, press Ctrl + C in the terminal where they are running, or run:

``` docker-compose down ```

 
