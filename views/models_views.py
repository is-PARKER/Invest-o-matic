import json
import flask
from flask import Request, jsonify, render_template, session, url_for

from infrastructure import irr
from infrastructure.other_calculations import get_net_return
from services.model_service import create_irr_model

from viewmodels.models.irr_viewmodel import IRRViewModel
from viewmodels.models.review_irr_viewmodel import ReviewIRRViewModel
from viewmodels.models.index_viewmodel import IndexViewModel
from viewmodels.models.noid_review_viewmodel import NoID_ReviewIRRViewModel
from viewmodels.models.noid_irr_viewmodel import NoID_IRRViewModel



blueprint = flask.Blueprint('models', __name__, template_folder='templates')


### NO login IRR ###

@blueprint.route('/models/noid/createirr', methods=['GET'])
def get_noid_irr():
    vm = NoID_IRRViewModel()

    return render_template('models/noid_createirr.html', **vm.to_dict())

@blueprint.route('/models/noid/createirr', methods=['POST'])
def post_noid_irr():
    vm = NoID_IRRViewModel()
    request_form = vm.request.form

    vm.project_name = request_form['project_name']
    vm.project_desc = request_form['project_desc']
    vm.comp_month = int(request_form['comp_month'])
    vm.asset_term = int(request_form['asset_term'])
    vm.yearly_return = int(request_form['yearly_return'])
    vm.invest_amt = int(request_form['invest_amt'])

    print(request_form)

    if not vm.project_name or not vm.comp_month or not vm.asset_term or not vm.yearly_return or not vm.invest_amt:
        return { 'error': 'Some fields appear to be missing.' }
    
    
    vm.invest_array, vm.return_array = irr.create_lists(months_until_completion=vm.comp_month,
                term_of_asset=vm.asset_term,
                yearly_return_amount=vm.yearly_return,
                investment=vm.invest_amt,
            )
    vm.irr_array, vm.irr = irr.irr_process(yearly_invest_array=vm.invest_array,yearly_return_array=vm.return_array)


    if vm.irr_array and vm.irr:
        try:
            flask.session['project_name'] = vm.project_name
            flask.session['project_name'] = vm.project_name
            flask.session['project_desc']  = vm.project_desc
            flask.session['comp_month'] = vm.comp_month
            flask.session['asset_term']= vm.asset_term
            flask.session['yearly_return']= vm.yearly_return
            flask.session['invest_amt'] = vm.invest_amt
            flask.session['irr'] = vm.irr
            flask.session['invest_array'] = json.dumps(vm.invest_array)
            flask.session['return_array'] = json.dumps(vm.return_array)
            flask.session['irr_array'] = json.dumps(vm.irr_array)
            #resp = flask.make_response(render_template('models/noid_reviewirr.html',**vm.to_dict()))
            resp = flask.redirect(url_for('models.noid_review',**vm.to_dict()))
            return resp

        except:
            vm.error = "There was problem with the modeling."

    return render_template('models/noid_createirr.html',**vm.to_dict())

@blueprint.route('/models/noid/reviewirr', methods=['GET','POST'])
def noid_review():
    vm = NoID_ReviewIRRViewModel()

    try:
        vm.project_name = flask.session.get('project_name')
        vm.project_desc = flask.session.get('project_desc')
        vm.comp_month = int(flask.session.get('comp_month'))
        vm.asset_term = int(flask.session.get('asset_term'))
        vm.yearly_return = int(flask.session.get('yearly_return'))
        vm.invest_amt = int(flask.session.get('invest_amt'))
        vm.irr = int(flask.session.get('irr'))

        vm.invest_array = json.loads(flask.session.get('invest_array'))
        print(f'invest array is {vm.invest_array}')
        vm.return_array = json.loads(flask.session.get('return_array'))
        vm.irr_array = json.loads(flask.session.get('irr_array'))
    
        vm.chart_array = irr.create_chart_array(vm.irr_array)
        

        labels = [row[0] for row in vm.chart_array]
        values = [row[1] for row in vm.chart_array]

        net_return = get_net_return(values)

        bar_color = []

        for i in values:
            if i > 0:
                bar_color.append('rgb(6, 219, 234)')
            else:
                bar_color.append('rgb(255,0,0)')

    except:
        vm.error = "Hmm. something didn't work here."
        print(vm.error)    

    return render_template('models/noid_reviewirr.html',labels=labels,bar_color=bar_color, values=values,net_return=net_return,**vm.to_dict())
    

### Logged in Create IRR ####

@blueprint.route('/models/createirr', methods=['GET'])
def get_irr():
    vm = IRRViewModel()


    return render_template('models/createirr.html',**vm.to_dict())

@blueprint.route('/models/createirr', methods=['POST'])
def post_irr():
    vm = IRRViewModel()
    request_form = vm.request.form

    vm.project_name = request_form['project_name']
    vm.project_desc = request_form['project_desc']
    vm.comp_month = int(request_form['comp_month'])
    vm.asset_term = int(request_form['asset_term'])
    vm.yearly_return = int(request_form['yearly_return'])
    vm.invest_amt = int(request_form['invest_amt'])

    print(request_form)

    if not vm.project_name or not vm.comp_month or not vm.asset_term or not vm.yearly_return or not vm.invest_amt:
        return { 'error': 'Some fields appear to be missing.' }
    
     
    vm.invest_array, vm.return_array = irr.create_lists(months_until_completion=vm.comp_month,
                term_of_asset=vm.asset_term,
                yearly_return_amount=vm.yearly_return,
                investment=vm.invest_amt,
            )
    vm.irr_array, vm.irr = irr.irr_process(yearly_invest_array=vm.invest_array,yearly_return_array=vm.return_array)

    if vm.irr_array and vm.irr:
        irr_model = create_irr_model(vm)
        model_id = irr_model.model_id
        resp = flask.redirect(url_for('models.review_irr',model_id=model_id))
        return resp

    return render_template('models/createirr.html',**vm.to_dict())


### Review a Specific IRR ###

@blueprint.route('/models/reviewirr/<int:model_id>', methods=['GET','POST'])
def review_irr(model_id:int):
    vm = ReviewIRRViewModel(model_id)

    if not vm.irr:
        return flask.abort(status=404)

    


    vm.irr.irr = round(vm.irr.irr,2)


    vm.irr_array = [
        (1,-20000),
        (2,-500),
        (3,4000),
        (4,80000),
        (5,40000),
        (6,30000),
        (7,20000),
        (8,40000),
        (9,20000),
        (10,40000)
    ]



    print(vm.model_id)

    labels = [row[0] for row in vm.irr_array]
    values = [row[1] for row in vm.irr_array]

    net_return = get_net_return(values)

    bar_color = []

    for i in values:
        if i > 0:
            bar_color.append('rgb(6, 219, 234)')
        else:
            bar_color.append('rgb(255,0,0)')

    return render_template('models/reviewirr.html',labels=labels,bar_color=bar_color, values=values,net_return=net_return,**vm.to_dict())

    
### Model Index ###

@blueprint.route('/models', methods=['GET','POST'])
def index():
    vm = IndexViewModel()

    return render_template('models/index.html',**vm.to_dict())
    
