# Adam~~Awwards

## Author
### [Abdimulhin Adan](https://github.com/AbdimulhinYussuf3675)

## Description
This is a web application that allows a user to post a project they have created and get it reviewed by his/her peers.


## User stories
>As a user I should be able to:

*  view posted projects and their details.
* rate/review other users' projects.
*  search for projects by their title.
*  view their profile page.


## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running

   ```bash
   git clone https://github.com/AbdimulhinYussuf3675/Awwards-.git
   ```
 or download a zip file of the project from github


Navigate to the project directory
```bash
cd Awwards
```

##### 2. Create a virtual environment

To create a virtual environment named `virtual`, run

   ```prettier
   python3 -m venv Virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```
##### 3. Create a django and create django projects
 Install django
 ```bash
 pip install django==1.11.17
  ```
  Create django project
  ```bash
  django-admin startproject awwards .
```
create a clone app
 ```bash
 django-admin startapp zawadi
 ```



##### 5. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```awards```
   ```
   # create database awards


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python manage.py makemigrations awwards
```


then run the command below;

 ```bash
 python manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine,

    python3 manage.py runserver

## Technologies Used
* Django
* Python
* Html
* Css
* Bootstrap3
* Django-Admin
* Cloudinary




## Bugs
* No known bugs.

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2021 Abdimulhin

# Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

# Contacts
adam.abdimulhi.001@gmail.com