from typing import Final, Optional, List
from datetime import datetime

from flask import session

import data.__db_session as db_session
from data.users import User
from data.models import Models
from data.irr import IRR


def create_irr_model(vm) -> Optional[User]:

    session = db_session.create_session()

    model = Models()

    model.user_id = vm.user_id
    model.project_name = vm.project_name
    model.project_desc = vm.project_desc
    model.date_created = datetime.now()
    model.type = "IRR"

    

    irr = IRR()

    irr.project_name = vm.project_name
    irr.project_desc = vm.project_desc
    irr.comp_month = vm.comp_month
    irr.asset_term = vm.asset_term
    irr.yearly_return = vm.yearly_return
    irr.invest_amt = vm.invest_amt

    # irr.return_array = vm.return_array
    # irr.invest_array = vm.invest_array
    # irr.irr_array = vm.irr_array

    irr.irr = vm.invest.amt
    

    try:
        session.add(model)
        session.flush()
        irr.model_id=model.model_id 
        session.add(irr)
        session.commit()
    finally:
        session.close()

    return irr

def find_irr_model_by_model_id(model_id:int):
    session = db_session.create_session()
    try:
        irr = session.query(IRR).filter(IRR.model_id==model_id).first()
        return irr
    finally:
        session.close()
    
def find_models():
    session = db_session.create_session()

    try:
        models = list(session.query(Models)).order_by(Models.model_id.desc)
        return models
    finally:
        session.close()

    