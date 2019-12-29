import csv
import os
from psycopg2 import sql, Error as psycopg2_Error
from datetime import datetime
from os.path import isfile, join
from db_simple import conn, cursor

folder_path = os.path.abspath('../travel_logs')


def fill_points(folder_path: str):
    try:
        folder_path = os.path.abspath(folder_path)
        files = [join(folder_path, f) for f in os.listdir(folder_path) if isfile(join(folder_path, f))]

        for file_name in files:
            with open(file_name, 'r') as f:
                reader = csv.reader(f)

                next(reader)  # This skips the 1st in csv row which is the header.
                for record in reader:
                    if not record:
                        continue

                    record_i = iter(record)
                    timepoint = next(iter(record_i), None)
                    longitude = next(iter(record_i), None)
                    latitude = next(iter(record_i), None)
                    event_name = file_name.split('/')[-1]

                    if timepoint:
                        timepoint = datetime.fromtimestamp(float(timepoint[:10]))

                    ST_MakePoint_str = None
                    if longitude and latitude:
                        longitude = float(longitude)
                        latitude = float(latitude)
                        ST_MakePoint_str = f'POINT({longitude} {latitude})'

                    cursor.execute(
                        sql.SQL("insert into {} (timepoint, geom, event_name) values (%s, ST_GeomFromText(%s, 4326), %s)").
                            format(sql.Identifier('points')), [timepoint, ST_MakePoint_str, event_name])

                conn.commit()
        return True
    except (Exception, psycopg2_Error) as e:
        # should be logger here
        print(e)


if __name__ == '__main__':
    folder_path = '../travel_logs'
    fill_points(folder_path)
