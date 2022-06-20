from flask import Flask, jsonify, redirect, url_for, session
from flask import render_template
from authlib.integrations.flask_client import OAuth
import os
import sys
import psycopg2
import sqlalchemy
from config import DATABASE_URL
from infrastructure.connection_fix import replace_postgres

# from config import DATABASE_URL


folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)


from data import __db_session as db_session

app = Flask(__name__)
app.secret_key='random_secret'
app.config.from_object('config')



def main():
    configure()
    app.run(debug=True, port=5006)

def configure():

    register_blueprints()

    setup_db()

def setup_db(): 

    #this_folder = os.path.dirname(os.path.abspath(__file__))
    #SQL_lite_connection = "sqlite:////" + os.path.join(this_folder,'db','test.sqlite')

    # conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    db_url_fixed = replace_postgres(DATABASE_URL)

    conn = db_url_fixed + "?sslmode=require"

    db_session.database_init(conn)

def register_blueprints():

    from views import account_views
    from views import models_views
    from views import home_views

    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(models_views.blueprint)
    app.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    main()
else:
    configure()





# @app.route('/')
# def homepage():
#     user = session.get('user')
#     return render_template('home.html', user=user)
# 
# 
# @app.route('/login')
# def login():
#     redirect_uri = url_for('auth', _external=True)
#     return oauth.google.authorize_redirect(redirect_uri)
# 
# @app.route('/auth')
# def auth():
#     token = oauth.google.authorize_access_token()
#     user = token.get('userinfo')
#     if user:
#         session['user'] = user
#     return redirect('/')
# 
# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect('/')
