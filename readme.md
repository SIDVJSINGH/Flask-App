# Flask APP
This project is a simple Flask Application project

# File Structure:
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

# Each file contains
``` application/templates/index.html```   : contains the basic HTML form for QUIZ questions without JINJA Templating
```application/__init__.py```   : contains the flask app object that is later used throughout the project
```application/all_question```  : hard coded Question objects with a list of 5 questions for Quiz
```application/question_class``` : contains Class structure of each question that is required in a Quiz with desired variables
```application/routes.py```  : contains the application routes to forward to
```Dockerfile``` : contains python-alpine image to run our Flask application on
```requirement.txt```: contains all required modules to run this Flask application on your local with the versions
```run.py``` : the main file that runs the application from outside.


# this application has a Docker Image on Docker Hub
Try following command to run this on your local:

 ``` docker run sidvjsingh/flask_app:latest ```
The above single command will pull the image from the Docker Hub and ran it in your local

alternatively you can also do

```
docker pull sidvjsingh/flask_app:latest
docker run sidvjsingh/flask_app:latest
```