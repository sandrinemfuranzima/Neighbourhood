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

### Behaviors

<ol>
    <li>The project has an admin dashboard, where I as the administrator manages all models.</li>
    <li>The User can join a neighbourhood by clicking the button "Join" on the homepage</li>
    <li>Once a user signs in, their profile is created automatically, and they can navigate to their profile by clicking on their profile name link on the navbar.</li>
    <li>The User can search for hoods they are interested in by typing the name of the hood location on the 'hood search bar' on the navbar. Once they join a hood,they can also search for a business in the respective neighbourhood by typing the name of the business in the 'hood business bar' on the navbar</li>
    <li>The User can create a Post in the neighbourhood and edit their post.</li>
    <li>The User can create a Business in the neighbourhood and edit their business.</li>
    <li>The User Profile is updated once the user joins a neighbourhood.</li>
</ol>



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
