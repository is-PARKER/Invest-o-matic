
import flask
from flask import render_template


from viewmodels.home.index_viewmodel import IndexViewModel
from viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
def index_home():
    vm = IndexViewModel()
    return render_template('home/index.html', **vm.to_dict())


@blueprint.route('/about')
def about_site():
    vm = ViewModelBase()
    return render_template('home/about.html', **vm.to_dict())