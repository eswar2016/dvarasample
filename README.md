

# Install pip first for python3
1. sudo apt-get install python3-pip

# Install virtualenv
2. sudo pip3 install virtualenv

# Create virtualenv using Python3
3. virtualenv -p python3 myenv

# Activate virtualenv.
4. source myenv/bin/activate

# Clone the project
5. git clone https://github.com/eswar2016/dvarasample.git

# install requirements - 
6. pip install -r requirements.txt

# Migrate the app
7. python manage.py migrate

# Run the server
8. python manage.py runserver


# Create superuser as admin to login
9. python manage.py createsuperuser

# upload sheet with category and subcategory as sheet names
10. http://127.0.0.1:8000/upload/

# Select Category to check the list of subcategories in home page
11. http://127.0.0.1:8000/