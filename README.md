# Setup (ENG)
## 1. Cloning repository 
First of all, you need to clone the project repository to your local computer. Use the git clone command:<br>
`git clone <repository URL>`
## 2. Create a virtual environment 
To create a virtual environment, use the command: <br>
`python -m venv <environment_name>`<br><br>
Activate the virtual environment:
- On Windows:
`.\venv\Scripts\activate`
- On macOS or Linux:
`source venv/bin/activate`
## 3. Installing dependencies
To install all the necessary libraries, run the command:<br>
`pip install -r requirements.txt`.
## Execute the next commands in the project directory of your choice. For example, to test the library API, navigate to it with `cd library`
## 4. Migrating the database 
After you create the virtual environment and activate it, you need to perform a database migration. This applies the changes that were defined in your project models to the database:<br>
`python manage.py migrate`<br>
If there are problems, then run the command:<br>
`python manage.py makemigrations`<br>
And then:<br>
`python manage.py migrate`
## 5. Creating a superuser
In order to access the Django admin panel, you need to create a superuser. This can be done with the following command:<br>
`python manage.py createsuperuser`
## 6. Starting the Django server 
To start the Django server and check the operation of your project, use the command:<br>
`python manage.py runserver`
