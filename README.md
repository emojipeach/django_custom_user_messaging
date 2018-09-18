[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a32d2b4bdf614c4587adee2134900c53)](https://www.codacy.com/app/emojipeach/django_custom_user_messaging?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=emojipeach/django_custom_user_messaging&amp;utm_campaign=Badge_Grade)

## A Django app for private messaging between users with a working custom User model implemented

Based on arneb/django-messages

* Updated to work on Django 2.1.1
* Message.id field changed to uuid4
* Removed features I don't need (email and pinax integration)
* Rewritten URLs to use path() rather than url()
* Added a custom User model
* Case insensitive username checking
* Added an example field to user model (pgp_key) with demo of how it is added to forms and admin
* User and Messaging apps are working properly in the admin panel