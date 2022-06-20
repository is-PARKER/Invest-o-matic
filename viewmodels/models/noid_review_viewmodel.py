from typing import Optional
from urllib import request

import flask 
from flask import request
from flask import Request

from viewmodels.shared.viewmodelbase import ViewModelBase

# Add user service.


class NoID_ReviewIRRViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
