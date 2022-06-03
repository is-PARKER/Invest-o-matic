from crypt import methods
from urllib import request
import flask
from flask import Request, render_template

from infrastructure import irr
from services.model_service import create_irr_model

from viewmodels.models.irr_viewmodel import IRRViewModel
from viewmodels.models.review_irr_viewmodel import ReviewIRRViewModel
from viewmodels.models.index_viewmodel import IndexViewModel



blueprint = flask.Blueprint('models', __name__, template_folder='templates')


### Create IRR ###

@blueprint.route('/models/createirr', methods=['GET'])
def get_irr():
    vm = IRRViewModel()
    request_form = vm.request.form
    vm.form = request_form

    return render_template('models/irr.html',**vm.to_dict())

@blueprint.route('/models/createirr', methods=['POST'])
def post_irr():
    vm = IRRViewModel()
    request_form = vm.request.form
    
    vm.project_name = request_form['project_name']
    vm.project_desc = request_form['project_desc']
    vm.comp_month = request_form['comp_month']
    vm.asset_term = request_form['asset_term']
    vm.yearly_return = request_form['yearly_return']
    vm.invest_amt = request_form['invest_amt']

    if not vm.project_name or not vm.comp_month or not vm.asset_term or not vm.yearly_return or not vm.invest_amt:
        return { 'error': 'Some fields appear to be missing.' }
    
    try: 
        vm.invest_array, vm.return_array = irr.create_lists(months_until_completion=vm.comp_month,
                    term_of_asset=vm.asset_term,
                    yearly_return_amount=vm.yearly_return,
                    investment=vm.invest_amt,
                )

        vm.irr_array, vm.irr = irr.irr_process(yearly_invest_array=vm.invest_array,yearly_return_array=vm.return_array)
    except:
        vm.error = "There was an issue processing the given data"

    if vm.irr_array and vm.irr:
        irr_model = create_irr_model(vm)
        id = irr_model.model_id
        resp = flask.redirect('/models/reviewirr/<id>')
        return resp

    return render_template('models/irr.html',**vm.to_dict())


### Review a Specific IRR ###

@blueprint.route('/models/reviewirr/<int:model_id>', methods=['GET','POST'])
def review(model_id:int):
    vm = ReviewIRRViewModel(model_id)
    if not vm.irr.model_id:
        return flask.abort(status=404)

    print(vm.model_id)

    return render_template('models/review.html', **vm.to_dict())

    
### Model Index ###

@blueprint.route('/models', methods['GET','POST'])
def index():
    vm = IndexViewModel()

    return render_template('models/index.html',**vm.to_dict())
    
    