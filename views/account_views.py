
import flask
from flask import Request, session, redirect, url_for
from flask import render_template, Blueprint
from authlib.integrations.flask_client import OAuth
from services.user_service import create_user, find_user_by_google_sub_id





blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
def index():
    from viewmodels.account.index_viewmodel import IndexViewModel
    vm = IndexViewModel()
    vm.db_user.created_date_day = vm.db_user.created_date.date()

    return render_template('account/index.html', **vm.to_dict())


@blueprint.route('/account/login')
def login():
    from infrastructure.oauth import oauth

    redirect_uri = url_for('account.auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@blueprint.route('/account/auth')
def auth():
    from infrastructure.oauth import oauth

    token = oauth.google.authorize_access_token()
    user = token.get('userinfo')
    email = user['email']
    google_sub_id = user['sub']
    if not find_user_by_google_sub_id(google_sub_id):
        create_user(email=email,google_sub_id=google_sub_id)

    if user:
        session['user'] = user
    
    return redirect('/')

@blueprint.route('/account/logout')
def logout():
    session.pop('user', None)
    return redirect('/')