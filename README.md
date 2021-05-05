## Description

As a user of the application, you are able to:
<ul>
    <li>Sign in to the application to start using.</li>
    <li>Set up a profile, a general location and a neighborhood name.</li>
    <li>Find a list of different businesses in my neighborhood.</li>
    <li>Create Posts that will be visible to everyone in my neighborhood</li>
    <li>Change My neighborhood when I decide to move out.</li>
    <li>Only view details of a single neighborhood.</li>
<ul>


## Features
- The home page allows users to see various images:
- User can see all images per location they were taken
- Users can also search for images based categories
- Admin can upload images from a django dashboard



## Technologies Used
    - Python 3.6
    - Django
    - HTML, CSS and Bootstrap3
    - JavaScript
    - Postgressql

### Prerequisite
The Sunsplash project requires a prerequisite understanding of the following:
- Django Framework
- Python3.6
- Postgres
- Python virtualenv

## Setup and installation

#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python3.6 as default handler
    `virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE gallery;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'gallery'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.6 manage.py makemigrations gallery
    python3.6 manage.py migrate
#### Run the app
    python3.6 manage.py runserver
    Open terminal on localhost:8000

## Known bugs
No known bugs so far. If found drop me an email.


## Contributors
    - Mfuranzima Sandrine

### Contact Information
mfuranzimasandri20@gmail.com
