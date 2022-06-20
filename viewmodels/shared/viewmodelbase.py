

from typing import Optional

import flask 
from flask import Request, session
from data.users import User
from services.user_service import find_user_by_google_sub_id


class ViewModelBase:
    def __init__(self):
        if session.get('user'):
            user_dict = session.get('user')
            self.google_sub_id = user_dict['sub']
            self.user_dict=user_dict
        
        self.error: Optional[str] = None

        self.request: Request = flask.request
       
    def to_dict(self):
        return self.__dict__