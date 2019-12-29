from commands.csv_to_db_points import fill_points
from extensions import db
from models.lines import Lines


if __name__ == '__main__':
    def model_exists(model_class):
        engine = db.get_engine(bind=model_class.__bind_key__)
        return model_class.metadata.tables[model_class.__tablename__].exists(engine)

    s = model_exists(Lines)
    folder_path = '../travel_logs'
    fill_points(folder_path)
