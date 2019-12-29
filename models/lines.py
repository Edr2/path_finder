from sqlalchemy import DateTime, Float, Column, String
from extensions import db
from models.geometry import Geometry


class Lines(db.Model):
    __tablename__ = 'lines'

    event_name = Column(String, primary_key=True)
    time_start = Column(DateTime)
    time_end = Column(DateTime)
    length_km = Column(Float)
    newgeom = Column(Geometry)
    hours = Column(Float)
