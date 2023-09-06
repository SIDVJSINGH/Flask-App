# Flask APP
This project is a simple Flask Application project.
I'm not so good with HTML and CSS, therefore used a simple HTML document.
This can be improved with the help of Bootstrap templates and Jinja Templating.

# File Structure:
```
Root
├───application
│    ├───templates
│    │         └───index.html
│    ├───__init__.py
│    │
│    ├───all_questions.py
│    │
│    ├───question_class.py
│    │
│    └───routes.py
│
├───Dockerfile
├───requirement.txt
├───readme.md
└───run.py
```

# Each file contains
- ```application/templates/index.html```   : contains the basic HTML form for QUIZ questions without JINJA Templating.
- ```application/__init__.py```   : contains the flask app object that is later used throughout the project.
- ```application/all_question```  : hard coded Question objects with a list of 5 questions for Quiz.
- ```application/question_class``` : contains Class structure of each question that is required in a Quiz with desired variables.
- ```application/routes.py```  : contains the application routes to forward to.
- ```Dockerfile``` : contains python-alpine image to run our Flask application on.
- ```requirement.txt```: contains all required modules to run this Flask application on your local with the versions.
- ```run.py``` : the main file that runs the application from outside.


# This application has a Docker Image on Docker Hub
Try following command to run this on your local after installing Docker Daemon:

``` 
docker run sidvjsingh/flask_app:1.1 
```
This single command will pull the image from the Docker Hub and ran it in your local.

Alternatively you can also do:
```
docker pull sidvjsingh/flask_app:1.1
```
```
docker run sidvjsingh/flask_app:1.1
```