from models.lines import Lines
from flask import Blueprint, jsonify
from sqlalchemy import func
from extensions import db

main_page = Blueprint('main_page', __name__)


@main_page.route("/")
def hello():
    lines_count = db.session.query(func.count(Lines.event_name)).scalar()
    roads = db.session.query(Lines.event_name).all()

    result = []

    for record in roads:
        result.append(record.event_name)

    return jsonify(result)
