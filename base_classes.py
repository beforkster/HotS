""" Sets up Base Classes for objects """
from data_pull import data_gather_dim
import os
import sys
dimension_list = ['waveclear', 'dmg_sustain', 'dmg_burst', 'tank', 'cc', 'support_sustain', 'support_save']
file = sys.argv[0]
path_name = os.path.dirname(file)
hots_db = os.path.join(path_name, 'hots.db')

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


    # def waveclear(self, wavelear_rating):
    #     "effective minion or camp waveclear - 100% avg scale"
    #     self.waveclear = waveclear_rating
    #
    # def dmg_burst(self, burst_score):
    #     """
    #         Very High Burst(high damaging burst, and much of it is aoe): 4
    #         High Burst(high damage burst with some AOE, or med burst all AOE): 3,
    #         Medium Burst(medium damage burst or high dmg on a slightly longer time frame): 2,
    #         Low Burst(noticeable amount of frontloaded dmg): 1
    #         No Burst(no noticeable frontloaded dmg): 0
    #     """
    #     self.dmg_burst = burst_score
    #
    # def dmg_sustain(self, dmg_sustain_score):
    #     "Overall DPS numbers - 100% avg scale per hero"
    #     self.dmg_sustain = dmg_sustain_score
    #
    # def tank(self, tank_score):
    #     "survivability - 100% avg scale per hero"
    #     self.tank = tank_score
    #
    # def cc(self, crowd_control):
    #     """
    #         Very Hard CC(lots of stun/aoe stuns): 4
    #         Hard CC(lots of slow/root or a few stuns): 3,
    #         Medium CC(silence/root/slow and a stun, etc): 2,
    #         Soft CC(noticeable slow/root/dmg_reduc/etc): 1
    #         No CC(little to no control): 0
    #     """
    #     self.cc = crowd_control
    #
    # def support_sustain(self, sup_sustain_score):
    #     "healing output - 100% avg scale per hero"
    #     self.support_sustain = sup_sustain_score
    #
    # def support_save(self, save_score):
    #     """
    #         Heavy Save(high ability to save someone): 3,
    #         Medium Save(medium save ability): 2,
    #         Some Save(noticeable save ability): 1
    #         No Save(little to no save ability): 0
    #     """
    #     self.support_save = save_score


# class Hero(Item):
#     """
#     Instances will be individual heroes with attributes representing all
#     relevant attributes of a hero that determine the contribution a hero has to
#     the success or failure of a game for their team
#     """
#
#     def __init__(self, hero_name):
#         self.name = hero_name
#         self.data_set(self, hero_name)
        # dimension_list = [method for method in dir(type(self).__bases__[0]) if not method.startswith('__')]
        # dimension_list = ['waveclear', 'dmg_sustain', 'dmg_burst', 'tank', 'cc', 'support_sustain', 'support_save']
        # self.name = hero_name
        # data = data_gather_dim(r'C:\Users\baxter\reader\apps\Hots\hots_data.db', dimension_list, [hero_name], 'hero_data', 'hero_name')
        # data = data[0]
        # self.waveclear = int(data[0])
        # self.dmg_sustain = int(data[1])
        # self.dmg_burst = int(data[2])
        # self.tank = int(data[3])
        # self.cc = int(data[4])
        # self.support_sustain = int(data[5])
        # self.support_save = int(data[6])

# class Map(Item):
#     """ Current Map in Game """
#
#     def __init__(self, map_name):
#         dimension_list = ['waveclear', 'dmg_sustain', 'dmg_burst', 'tank', 'cc', 'support_sustain', 'support_save']
#         self.name = hero_name
#         data = data_gather_dim(r'C:\Users\baxter\reader\apps\Hots\hots_data.db', dimension_list, [hero_name], 'hero_data', 'hero_name')
#         data = data[0]
#         self.waveclear = int(data[0])
#         self.dmg_sustain = int(data[1])
#         self.dmg_burst = int(data[2])
#         self.tank = int(data[3])
#         self.cc = int(data[4])
#         self.support_sustain = int(data[5])
#         self.support_save = int(data[6])
