# HarmonyVerse
HarmonyVerse is a music app that harmonizes your world with the power of music. Seamlessly integrated with the Spotify API, HarmonyVerse opens up a universe of musical possibilities, allowing you to immerse yourself in a harmonious journey like never before.

<h3 align="left">Languages and Tools:</h3>
<p align="left"><a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> </p>

# Getting started 
To set up and run the Django project locally, follow these steps:

## Installation

Install Django with pip

```bash
  pip install django
```

After downloading Django

Clone this repository using git command:
```bash
  git clone [url]
```
Open the directory where the repository is stored:
```bash
  cd dir
```
Once you are in the directory, run the following command in terminal:
```bash
  cd HarmonyVerse
```

Before running the project on browser you should generate an authorizarion token from authToken.py file and add that access token in app/views.py in format headers={
    'Content-Type':'application/json',
    'Authorization': 'Bearer {TOKEN}'
}.

Now the project is ready to run on your local device.
 1. Open Terminal and run
```bash
  python manage.py runserver
```
 2. Open a web browser of choice and go to http://localhost:8000/ . You
should see the home page for our website!

You can now start working on adding features or fixing bugs by making changes directly inside `HarmonyVerse`!!