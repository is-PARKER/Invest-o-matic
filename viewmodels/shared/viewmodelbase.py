
from typing import Optional

import flask 
from flask import Request, session
from data.users import User
from services.user_service import find_user_by_google_sub_id

class ViewModelBase:
    def __init__(self):
        self.user_dict: Optional[dict] = None
        self.user: Optional[User] = find_user_by_google_sub_id(self.user_dict['sub'])
        self.request: Request = flask.request
        #consdier adding request dictionary. 
        self.error: Optional[str] = None
       
    def to_dict(self):
        return self.__dict__