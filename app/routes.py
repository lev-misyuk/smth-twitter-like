from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lev'}
    posts = [
        {
            'author': {'username': 'Lev'},
            'body': 'Beautiful day in Moscow!'
        },
        {
            'author': {'username': 'aaa'},
            'body': 'bbb'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
