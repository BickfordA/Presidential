from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Aidan'}

    posts = [ # fake array of presidents
        {
            'author' : {'nickname' : 'John'},
            'body': 'My last name is john'
        },
        {
                    'author' : {'nickname' : 'Bill'},
                    'body': 'My first name is bill'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user = user,
                            posts = posts)
