# AdNabu Challenge

This project is done as part of AdNabu challenge. This Provides an API to download
contenets of provided urls and send it to a given email id.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project runs on django 1.11 and python 3.5, the required packages are provided in
requirements.txt file

### Installing

1) Download the project.
2) Install RabbitMQ.
3) Create a virtual environment.
4) Switch to virtual environment.
5) In project directory run "pip install -r requirements.txt".
6) In project directory add folder named adnabu_dow and give write access.
7) configure database and smtp
8) Generate and run migration scripts and start project using "python manage.py runserver"
9) start celery using "python manage.py cleryd -B -E --loglevel=info"