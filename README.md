# Artfolio

# Overview

Artfolio is a small project to keep the artistic activities of our artists so that we never forget them

# Features

- [x] Notification system : This project uses the notification system in the form of SMS and email, and we use RabbitMQ and Celery to ensure that all messages are sent successfully and no notification is missed.
- [x] JWT Authentication : It uses JWT tokens to authenticate users, which works on platforms other than the web.
- [x] Clear structure : The code is written in a way that is easy to understand and modify.


# Getting Started

## Requirements

- Python 3.8 and above
- Postegras or any other database supported by Django
- Rabbitmq 3.8.2

  ## Installation
  ### Step one:
  1. Clone the repository<br/>
   ```git clone https://github.com/mahdiashtian/artfolio.git```
  2. Navigate to the project directory<br/>
   ```cd artfolio```
  3. Create and activate a virtual environment<br/>
      1. ```sudo apt install python3.10-venv``` (Linux)
      2. ```python -m venv venv```
      3. ```source venv/bin/activate``` (Linux)
         ```venv\Scripts\activate``` (Windows)
  4. Install the requirements<br/>
     ```pip install -r requirements.txt```
  ### Step two:
  So far you have installed the project requirements and created a virtual environment, the next step is to install and configure Nginx and Gunicorn.
How to install and configure these two tools along with the database is fully explained in [this link](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu) below, After completing the first step, continue the tutorial from the above link to complete the project

# Contact
For any questions or suggestions, please contact [me](mailto:mahdiashtian.mo@gmail.com)
