# Tips 

### Running SetUp 
- For getting started source Inhancer/bin/activate 
- django-admin startproject Enhancer -> for Ubuntu 
- python manage.py migrate -> for making migrations 
- python manage.py runserver -> To run server 
- python manage.py create superuser -> set admin privi 
- python manage.py makemigrations -> create information to go on db 
- python manage.py migrate -> to push to the db 

### Templates 
- creating templates requires a directory structure to be followed for easier use 
```
	-AppName
		-templates 
			-AppName
				-file.html
```
- You can also have have other html files inheriting from a main file 
- {% extends 'AppName/main.html' %}
