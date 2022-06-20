from typing import Optional

import flask 
from flask import Request

from viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
       

        from services.model_service import find_models

        self.models = find_models()   
        