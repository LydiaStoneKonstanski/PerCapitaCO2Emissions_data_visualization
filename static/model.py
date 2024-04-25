from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqalchemy import SQAlchemy

db = SQAlchemy()

class Visuals(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.varchar(120), nullable=False)


def __init__(self, title):
    self.title = title

#TODO does this need anything to return it?

class Content(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    words = db.Column(db.varchar(999), nullable=False)

def __init__(self, title):
    self.words = words

#TODO does this need anything to return it?


