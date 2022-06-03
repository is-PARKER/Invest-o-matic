from typing import Optional

import flask 
from flask import Request

from viewmodels.shared.viewmodelbase import ViewModelBase

# Add user service.


class ReviewIRRViewModel(ViewModelBase):
    def __init__(self,model_id: int):
        super().__init__()
        self.model_id = model_id

        if model_id:
            from services import model_service
            self.irr = model_service.find_irr_model_by_model_id(self.model_id)
            if not self.irr:
                return None


        else:
            self.error = "Game is not created"        

