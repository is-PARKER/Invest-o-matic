from contextlib import nullcontext
import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey, false
from sqlalchemy.orm import relationship
from datetime import datetime

from data.modelbase import Base

class Models(Base):
    __tablename__ = 'models'

    model_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey("user.user_id"))
    project_name = sqlalchemy.Column(sqlalchemy.Text)
    project_desc = sqlalchemy.Column(sqlalchemy.Text)
    date_created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now() ,nullable=False)
    type = sqlalchemy.Column(sqlalchemy.Text, default="IRR")
    private_setting = sqlalchemy.Column(sqlalchemy.Boolean, default=False)


    irr = relationship("IRR",backref="models")
  

