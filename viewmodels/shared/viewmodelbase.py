
from typing import Optional

import flask 
from flask import Request, session


class ViewModelBase:
    def __init__(self):
        self.user = None
        self.request: Request = flask.request
        #consdier adding request dictionary. 
        self.error: Optional[str] = None
       
    def to_dict(self):
        return self.__dict__