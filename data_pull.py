import sqlite3
from base_classes import hots_db
conn = sqlite3.connect(hots_db)
c = conn.cursor()
m = ['waveclear', 'dmg_sustain', 'tank', 'cc']
i = ['Alarak', 'Chen', 'Stukov', 'Jaina', 'Valla']
t = 'hero_data'
im = 'hero_name'

def data_gather_dim(cxn, metric_list, itemname_list, table_name, itemtype_field):
    """ Retrieves sqldata for hero/map """
    query = 'SELECT {} FROM {} WHERE {} IN ({})'.format(', '.join(metric for metric in metric_list), table_name, itemtype_field, ', '.join('?' * len(itemname_list)))
    with sqlite3.connect(cxn):
        c = sqlite3.connect(cxn).cursor()
        c.execute(query, itemname_list)
        return(c.fetchall())

def Hero_List(cxn):
    """ Retrieves every Hero """
    query = 'SELECT hero_name from hero_data'
    with sqlite3.connect(cxn):
        c = sqlite3.connect(cxn).cursor()
        c.execute(query)
        return([result[0] for result in c.fetchall()])
