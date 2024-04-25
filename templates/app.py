from flask import render_template, redirect, request
from flask_mysqldb import MySQL
from . import create_app
#TODO from co2.models import...

app = create_app()

app.config['SITE NAME'] = 'Visualizing CO2 Emissions'
app.config['SITE DESCRIPTION'] = ''
app.config['FLASK_DEBUG'] = 1
