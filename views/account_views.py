from crypt import methods
import flask
from flask import Request
from flask import render_template


from infrastructure.forms import RegisterUserForm, LoginForm
from infrastructure.cookie_auth import set_auth_username, logout_username
from services import user_service



from viewmodels.account.index_viewmodel import IndexViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel
from viewmodels.account.login_viewmodel import LoginViewmodel
from viewmodels.shared.viewmodelbase import ViewModelBase



blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account')
def index():
    vm = IndexViewModel()
    print(vm.username)
    if not vm.username:
        return flask.redirect('/account/login')
        
    return render_template('account/index.html', **vm.to_dict())


### Register ###
@blueprint.route('/account/register', methods=['GET'])
def register_get():
    vm = RegisterViewModel()
    request_form = vm.request.form
    form = RegisterUserForm(request_form)
    vm.form = form

    return render_template('account/register.html', **vm.to_dict())

@blueprint.route('/account/register', methods=['POST'])
def register_post():
    vm = RegisterViewModel()
    request_form = vm.request.form
    form = RegisterUserForm(request_form)
    vm.form = form

    if form.validate():
        vm.username = form.username.data
        vm.email = form.email.data
        vm.password = form.password.data

        user = user_service.create_user(form.username.data,form.email.data,form.password.data)

        if not user:
            vm.error = "User Invalid!"
    
        resp = flask.redirect('/account')
        set_auth_username(resp,vm.username)
        
        return resp
    
    return render_template('account/register.html', **vm.to_dict())



### Login ###
@blueprint.route('/account/login', methods=['GET'])
def login_get():
    vm = LoginViewmodel()
    if vm.username:
        resp = flask.redirect('/account')
        return resp

    request_form = vm.request.form
    form = LoginForm(request_form)
    vm.form = form

    return render_template('account/login.html', **vm.to_dict())

@blueprint.route('/account/login', methods=['POST'])
def login_post():

    vm = LoginViewmodel()
    
    request_form = vm.request.form
    form = LoginForm(request_form)

    if form.validate():
        vm.username = form.username.data
        vm.password = form.password.data

        user = user_service.login_user(form.username.data, form.password.data)

        if not user:
            vm.error = "User Invalid!"
       
        else:
            resp = flask.redirect('/account')
            set_auth_username(resp, user.username)
            return resp

    vm.form = form

    return render_template('account/login.html', **vm.to_dict())


### Logout ###

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    logout_username(resp)
    return resp
            