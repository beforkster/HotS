""" Sets up Base Classes for objects """
from data_pull import data_gather_dim, hots_db
dimension_list = ['waveclear', 'dmg_sustain', 'dmg_burst', 'tank', 'cc', 'support_sustain', 'support_save']

class Item():
    """ All attributes of a map/hero/team necessary for a team to win """

    def __init__(self, item_name, item_type, dimensions=dimension_list, database=hots_db):
        self.name = item_name
        self.rating = 0
        if item_type == 'hero':
            field_table = 'hero_data'
            field_name = 'hero_name'
        elif item_type == 'map':
            field_table = 'map_data'
            field_name = 'map_name'
        else:
            raise ValueError('Invalid item_type. Must be "hero" or "map"')
        data = data_gather_dim(database, dimensions, [item_name], field_table, field_name)
        data = data[0]
        for num, dimension in enumerate(dimension_list):
            setattr(self, dimension, data[num])

    def __repr__(self):
        return '{} - {}'.format(self.__class__.__name__, self.name)

    def clr_rating(self):
        self.rating = 0

class Team(Item):
    """ Contains Heroes as members and a team rating based on the individual rating methods of Item """

    def __init__(self, teamname, member_list=None, dimensions=dimension_list):
        self.name = teamname
        if member_list is None:
            self.members = []
        else:
            self.members = member_list
        self.bans = []
        for dimension in dimension_list:
            setattr(self, dimension, 0)

    def member(self, member_name):
        for item in self.members:
            if item.name == member_name:
                return item

    def __len__(self):
        return len(self.members)

    def add_hero(self, hero1, dimensions=dimension_list):
        print(self.name)
        self.members.append(hero1)
        for dimension in dimension_list:
            setattr(self, dimension, getattr(hero1, dimension))

    def remove_hero(self, hero_name):
        try:
            self.members.remove(self.member(hero_name))
        except ValueError:
            print('Hero not on Team')

    def __repr__(self):
        return 'Team: {}'.format(member for member in self.members)

    def max_members(self):
        return sorted([member for member in self.members], key = lambda x: x.rating, reverse=True)[:3]

    def new_ban(self, hero2):
        self.bans.append(hero2)


class Game():
    """ Home Team, Enemy Team, Potential Team, Map """

    def __init__(self, hometeam, enemyteam, potentialteam, current_map):
        self.home_team = hometeam
        self.enemy_team = enemyteam
        self.pool = potentialteam
        self.map = current_map
