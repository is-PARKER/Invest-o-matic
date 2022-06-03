from typing import Optional

import flask 
from flask import Request
from viewmodels.shared.viewmodelbase import ViewModelBase



# Add user service.


class IRRViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.project_name: Optional[str] = None
        self.project_desc: Optional[str] = None
        self.comp_month: Optional[int] = None
        self.asset_term: Optional[int] = None
        self.yearly_return: Optional[float] = None
        self.invest_amt: Optional[float] = None



        self.irr: Optional[float] = None
        self.return_array: Optional[list] = None
        self.invest_array: Optional[list] = None
        self.irr_array: Optional[list] = None

