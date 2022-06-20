from email.policy import default
from enum import unique
import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from data.modelbase import Base

class IRR(Base):
    __tablename__ = 'irr'

    irr_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    model_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey("models.model_id"), unique=True, nullable=False)
    project_name = sqlalchemy.Column(sqlalchemy.Text)
    project_desc = sqlalchemy.Column(sqlalchemy.Text)
    model_type = sqlalchemy.Column(sqlalchemy.Text, default="IRR")
    private_setting = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    date_created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now() ,nullable=False)

    comp_month  = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=False)
    asset_term = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    yearly_return = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    invest_amt = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    return_array = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.Float))
    invest_array = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.Float))
    irr_array = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.Float))
    irr = sqlalchemy.Column(sqlalchemy.Float,nullable=False)

