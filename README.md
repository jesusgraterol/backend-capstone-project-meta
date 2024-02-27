# Meta: Back-End Capstone Project

This repository serves as my personal submission for the [Back-End Capstone Project](https://www.coursera.org/learn/back-end-developer-capstone?specialization=meta-back-end-developer) offered by Meta through Coursera in the [Back-End Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer).



![Postman Workspace](./workspace.png)


## Project Structure

```
backend-capstone-project-meta
    │
    littlelemon/
    │    ├───littlelemon/
    │    │       ├───asgi.py
    │    │       ├───settings.py
    │    │       ├───urls.py
    │    │       └───wsgi.py
    │    ├───reservation/
    │    │       ├───admin.py
    │    │       ├───apps.py
    │    │       ├───models.py
    │    │       ├───permissions.py
    │    │       ├───serializers.py
    │    │       ├───tests.py
    │    │       ├───urls.py
    │    │       └───views.py
    │    └───manage.py
    │
    README.md
```





## Getting Started

```bash
$ cd backend-capstone-project-meta/@TODO

$ pipenv shell

$ pipenv install

$ python3 manage.py makemigrations 

$ python3 manage.py migrate

$ python3 manage.py runserver
```





## MySQL User Credentials

**User:** `admindjango`

**Password:** `employee@123!`





## `superuser` Credentials

**Username:** `admin`

**Email:** `admin@littlelemon.com`

**Password:** `admin@123!`





## Endpoints

[Postman Workspace](https://www.postman.com/jesusgraterol/workspace/backend-capstone-project)




## Grading Criteria

1. [ ] Does the web application use Django to serve static HTML content?
2. [ ] Has the learner committed the project to a Git repository?
3. [ ] Does the application connect the backend to a MySQL database?
4. [ ] Are the menu and table booking APIs implemented?
5. [ ] Is the application set up with user registration and authentication?
6. [ ] Does the application contain unit tests?
7. [ ] Can the API be tested with the Insomnia REST client?