from typing import Optional

import flask 
from flask import Request
from viewmodels.shared.viewmodelbase import ViewModelBase



# Add user service.


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        