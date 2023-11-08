# Image system 

This repository is about a image system to run in the cloud. 

Using python and django, an API is created. The idea is expose a button to load an image, save them and show all images in the bucket. 

## Steps to create the docker image. 

We coud use the next comand to create de image. 

`docker build -t my-image-system . `

### Tips to local develop 
Don't forget to run migrations to create the database table for this model:

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 