""" Sets up Base Classes for objects """

class Item():
    """ All attributes of a map necessary for a team to win """

    def __init__(self, item_name):
        self.name = item_name

    def waveclear(self, wavelear_rating):
        self.waveclear = waveclear_rating

    def movement(self, movement_rating):
        self.movement = movement_rating

    def camps(self, camp_rating):
        self.camps = camp_rating

    def __repr__(self):
        return '{} - {}'.format(self.__class__.__name__, self.name)


class Map(Item):
    """ All attributes of a map necessary for a team to win """

    def __init__(self, map_name, obj_name):
        self.name = map_name
        self.obj = obj_name


class Hero(Item):
    """
    Instances will be individual heroes with attributes representing all
    relevant attributes of a hero that determine the contribution a hero has to
    the success or failure of a game for their team
    """
    def __init__(self, hero_name):
        self.name = hero_name

    def dmg(self, dmg_score):
        self.dmg = dmg_score

    def tank(self, tank_score):
        self.tank = tank_score

    def support(self, support_score):
        self.support = support_score

    def obj_score(self, obj_rank):
        self.obj_score = obj_rank


class Team(Hero):
    """ Home Team, Enemy Team, Potential Team """


    def __init__(self, member_list=[], waveclear_rating=0, movement_rating=0, camp_rating=0, dmg_score=0, tank_score=0, support_score=0):
        self.members = member_list
        self.waveclear = waveclear_rating
        self.movement = movement_rating
        self.camps = camp_rating
        self.dmg = dmg_score
        self.tank = tank_score
        self.support = support_score

    def team_type(self, team_type_id):
        self.team_type = team_type_id

    def __len__(self):
        return len(self.members)

    def add_hero(self, hero_name):
        self.members.append(hero_name)
        self.waveclear += hero_name.waveclear
        self.movement += hero_name.movement
        self.camps += hero_name.camps
        self.dmg += hero_name.dmg
        self.tank += hero_name.tank
        self.support += hero_name.support
        if self.team_type != 'Potential':
            assert len(self) < 6
        else:
            pass

    def remove_hero(self, hero_name):
        try:
            self.members.remove(hero_name)
        except ValueError:
            print('Hero not on Team')

    def __repr__(self):
        return "Team: " + "{}".format(self.members)
