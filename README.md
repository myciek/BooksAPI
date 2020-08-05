# BooksAPI
Recruitment task in Django

## Local instalation:
- clone repository
- move to the repo direction
- edit .env.template file and add your variables to connect with database and secret key
- change name of .env.template to .env
- in docker-compose.yml db service environment should be the same as in .env file
- run ```docker-compose up --build``` (it will populate database and run app)
- go to ```http://localhost:8003/<endpoint>``` to use application

## Endpoints:
- ```/books``` - [GET] list of all books.\
    <b>Optional parameters</b>:
    - filtring: ```/books?<filter>=<data>``` where ```<filter>``` can be ```author``` or ```published_date```
    - sorting: ```/books?ordering=published_date" - from oldest or ```/books?ordering=-published_date``` from newest
  
- ```/books/<id>``` - [GET] retrieve book with given id
- ```/db``` - [POST] with {"q": "war"} body - fill database with new books and update existing ones

## Testing:
- run ```docker-compose run api python manage.py test``` to start tests

## Development choices
- I decided to use ArrayField for authors and categories instead of using ManyToMany fields, becouse i didin't have to use this fields in any cases that needed seperate models.

