from typing import Optional

import flask 
from flask import Request
from services.user_service import find_user_by_google_sub_id, find_user_by_id
from viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        self.user = find_user_by_google_sub_id(self.user) # Have to check how the User is returned.