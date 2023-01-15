#!/bin/bash

cd [PATH/TO/PARENT/DIRECTORY];
source venv/bin/activate;
cd MigrationCenter;
python manage.py test;
gulp;