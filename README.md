# weblog
welcome to my project repository.<br>
This project is a weblog site that manage a lot of users and posts in different levels and categories.
Go on reading this file and start to have your own weblog by downloading this project.<br><br>

## Set Up The Project
> ### First , Download and Simple settings
> - Download or Clone the project repository and `cd` to it.
> - Go to root **local_settings.sample.py** of project and change the database info with your owns and set a strong secret key.
> - create a **venv** and activate it by these commands : `py -3 -m venv venv` then `venv\Scripts\activate` .
> - install requirement packages by `pip freeze > requirements.txt` .
<br />
<br />

>> ### Second, Complete your Database
>> - Create all ypur models by this command: `python manage.py migrate` .
>> - Create a "superuser" as an admin by : `pythonmanage.py createsuperuser` .
>> - Create standard weblog groups and set permissions for them by : `python manage.py create_group`
>> + write `--help` after this coomand to see all abalities !
>> - Again update your database with commands : `python manage.py makemigrations ` then `python manage.py migrate`
<br />
<br />

>>> ### Third and Last Step
>>> - Run project with : `python manage.py runserver`
>>> - With admin account log in to the admin site on url "/admin" .
>>> - Create some sample users and set the groups and permissions for them .
>>> - Site pages start on address "/myblog" ; go and browse as you want ...
<br />
<br />

## Description
This project built by [django](https://www.djangoproject.com/) as a framework and [python](https://www.python.org/) as a programming language.<br />
I try to speed up it and make sure about it's security, but if you have any recommandations or get into truble with my site write for me with [email](eshagh.farrokhi@yahoo.com).
This project is completely built by ***Eshaq Farrokhi*** in **March 2021**.
<br />
<br />
Thank you so much to read this file and choose our project ...<br />
Good Luck
