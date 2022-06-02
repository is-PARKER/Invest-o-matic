import flask
from flask import Request, render_template

from infrastructure import irr


blueprint = flask.Blueprint('models', __name__, template_folder='templates')

@blueprint.route('/models/irr', methodsp=['GET'])
def get_irr():
    vm = IRRViewmodel()
    request_form = vm.request.form
    form = IRRViewmodel(request_form)
    vm.form = form

    return render_template('models/irr.html',**vm.to_dict())




@blueprint.route('/models/irr', methodsp=['POST'])
def post_irr():
    vm = IRRViewmodel()
    request_form = vm.request.form
    form = IRRViewmodel(request_form)
    vm.form = form

    return render_template('models/irr.html',**vm.to_dict())


@blueprint.route('/models/review', methods=['GET'])
def get_review():
    vm = IndexViewmodel()
    