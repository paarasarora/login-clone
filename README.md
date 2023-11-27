### Login clone
## Description
This Django project is a web application that provides user authentication through Django Rest Framework (DRF) and Social Authentication. Users can sign up using either the traditional email and password method or through social authentication providers. Once signed up, users receive a verification email with a temporary token that needs to be confirmed to activate their account. Verification email will only be sent during token authentication. 

## Technologies Used
````
Django
Django Rest Framework
Social Auth
Mysql (RDS)
AWS (EC2, RDS)
Nginx
Gunicorn
````
Installation
Clone the repository:

`git clone https://github.com/yourusername/yourproject.git`
`cd login-clone`
#### Install dependencies using Pipenv:

`pip install virtualenv`

#### Next, create a virtual environment for your project. Replace <env_name> with your preferred name:
`virtualenv <env_name>`

### Install Project Dependencies
Navigate to the project directory and install the required packages using pip and the provided requirements.txt file:

`cd login-clone`

`pip install -r requirements.txt`

#### Apply migrations:


`python manage.py migrate`
Start the development server:


`python manage.py runserver`

Configuration


Usage

### API Endpoints

#### Signup Endpoint:

Endpoint: http://127.0.0.1:8000/api/signup/

Prod Endpoint: http://44.202.70.199/api/signup/

Method: POST

Parameters:
username
email
password
#### Login Endpoint:

Endpoint: http://127.0.0.1:8000/api/signup/

Prod Endpoint: http://44.202.70.199/api/verify/bybu9d-031a7dd0794f06df0715d9b3b9d6293e/

Method: POST

Parameters:
username or email
password
#### Email Verification Endpoint:

Endpoint: http://127.0.0.1:8000/api/verify/bybu9d-031a7dd0794f06df0715d9b3b9d6293e/

Prod Endpoint: http://44.202.70.199/api/verify/bybu9d-031a7dd0794f06df0715d9b3b9d6293e/

Method: GET

Parameters: token (received in the verification email)

#### Postman Collection

https://www.postman.com/dark-zodiac-789458/workspace/woro/collection/19572418-b9657640-4755-4c4a-a3f0-e9e223e861f9?action=share&creator=19572418


### Contact

For any issues or inquiries, please contact paarasarora2@gmail.com


