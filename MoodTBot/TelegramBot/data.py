from db import init_db, get_list_of_places, add_place

import sqlite3


def update_data_base():
    with sqlite3.connect('placelist.db') as conn:
        init_db(conn=conn, force=True)
    osm = osmparse()
    for i in range(len(osm)):
        name = osm[i]['title']
        rating = osm[i]['rating']
        link = findlink(name)
        with sqlite3.connect('placelist.db') as conn:
            add_place(conn=conn,
                      category_id=1,
                      name=name,
                      rating=rating,
                      link=link)


update_data_base()
