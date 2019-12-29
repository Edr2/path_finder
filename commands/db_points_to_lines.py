from db_simple import conn, cursor

query = """
insert into lines
select subq.event_name,
		subq.time_start,
		subq.time_end,
		ST_Length(subq.newgeom::geography)/1000 as length_km,
		subq.newgeom,
		EXTRACT(EPOCH FROM subq.time_end-subq.time_start)/3600 as hours
		FROM (
	SELECT gps.event_name,
	ST_MakeLine(gps.geom ORDER BY timepoint) AS newgeom,
	MIN(gps.timepoint) as time_start,
	MAX(gps.timepoint) as time_end
	FROM points AS gps
	GROUP BY gps.event_name
) as subq
"""

cursor.execute(query)
conn.commit()
