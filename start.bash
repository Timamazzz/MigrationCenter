#!/bin/bash

cd [PATH/TO/PARENT/DIRECTORY];
source venv/scripts/activate;
python manage.py runserver;
gulp;