# Schedula
### 1-About:
> Schedula is a backend service booking platform built with Django and Django Rest Framework.
> It enables customers to discover service providers, manage bookings and interact through a secure RESTful API.
___
### 2-Project Status: 
Under Development
___
### 3-Features:
#### Authentication
- User registration
- JWT authentication
- Login & Logout
- Token refresh
- User profile management
#### Provider Management
- Provider profile
- Public provider page
#### Service Management (In Progress)
- Create services
- Update services
- Delete services
#### Booking (Planned)
- Book a service
- Cancel booking
- Booking history
#### Reviews (Planned)
- Provider reviews
- Ratings
___
### 4-Tech Stack:
- Python
- Django
- Django Rest Framework
- PostgreSQL
- JWT Authentication
- Docker
- drf-spectacular
- React
___
### 5-Project Structure:
```
schedula/
|__ accounts/
|__ providers/
|__ services/
|__ bookings/
|__ reviews/
|__ config/
|__ manage.py
```
___
### 6-Installation
#### Requirements
> you must have **node** and **python3.14** installed on your system
> and if want to use postgreSQL you must have postgres installed
#### Clone the repository
```
git clone <repository-url>
cd Schedula/backend
```
#### Create virtual environment
```
python -m venv venv
```
#### Activate virtual environment
Linux/macOS
``` 
source .venv/bin/activate
```
Windows
``` 
.venv/Scripts/activate
```
#### Install dependencies
``` 
pip install -r requirements.txt
```
#### Create a `.env` file in location: **Schedula/backend/config/.env**
linux
```
touch config/.env
```
windows(CMD)
``` 
type nul > config/.env
```
#### Create the secret_key
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
#### Get the key and copy/paste in **.env** file
``` 
SECRET_KEY = 'copied key'
```
#### Setup smtp server environment variables
```
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your app password'
```
#### Setup postgres environment variables(if you have postgres)
``` 
DB_NAME=database name
DB_USER= database owner name
DB_USER_PASS= database owner password
DB_PORT= port (usually 5432 in localhost)
DB_HOST= host name (in your system 'localhost')
```
#### Create log file
linux
``` 
mkdir logs
touch logs/app.log
```
windows(CMD)
``` 
mkdir logs
type nul > logs/app.log
```
#### Apply migrations
``` 
python manage.py migrate
```
#### Run the server
``` 
python manage.py runserver
```
___
### 7- Environment variables
Create a ```.env``` file and configure your environment variables
___
### 8- API Documentation
OpenAPI Schema
``` 
/api/schema/
```
Swagger UI
``` 
/api/schema/swagger-ui/
```
ReDoc
``` 
/api/schema/redoc/
```
___
### 9- Roadmap
1. Authentication
2. Provider Profile
3. Service Management
4. Booking System
5. Payments
6. Reviews
7. Notifications
8. Docker Deployment
9. CI/CD
10. Automated Test
___
### 10-License
>This project is developed for learning and portfolio purposes

