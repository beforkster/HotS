import sqlite3
from base_classes import Item, Team, Game
from data_pull import Hero_List
hots_db = r'C:\Users\baxter\reader\apps\Hots\hots_data.db'

def game_start():
    # curmap = user('What is the map?')
    curmap = 'Battlefield of Eternity'
    herolist = Hero_List(hots_db)
    heroclasses = []
    for item in herolist:
        heroclasses.append(Item(item, 'hero'))

    game1 = Game([],[],[],'')
    game1.map = Item(curmap, 'map')
    game1.pool = Team(heroclasses, )
    print(game1.pool.member('Chen').waveclear)
    return game1

game_start()

def rank_members(team_obj, map_obj):
    pass
