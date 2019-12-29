from sqlalchemy import DateTime, Column, Integer
from extensions import db
from models.geometry import Geometry


class Points(db.Model):
    __tablename__ = 'points'

    id = Column(Integer, primary_key=True)
    event_name = Column(db.String)
    timepoint = Column(DateTime)
    geom = Column(Geometry)
