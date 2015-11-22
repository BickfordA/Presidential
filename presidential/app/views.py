from flask import render_template
from app import app
from app import db
from sqlalchemy import create_engine, MetaData, Table
from .models import Canidate

@app.route('/')
@app.route('/index')

def index():
    #can = Canidate.query.all()
    #print can

    #Canidate = Table('CANDIDATE', db.Model.metadata, autoload = True, autoload_with = db.engine)

    print Canidate.name
    print Canidate.columns
    print Canidate.c['Lname']



    user = {'nickname': 'Aidan'}

    posts = [ # fake array of presidents
        {
            'author' : {'nickname' : 'a' },
            'body': 'My last name is a'
        },
        {
                    'author' : {'nickname' : 'Bill'},
                    'body': 'My first name is b'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user = user,
                            posts = posts)
