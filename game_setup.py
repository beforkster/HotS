import sqlite3
from base_classes import Item, Team, Game, hots_db, dimension_list
from data_pull import Hero_List

def game_start():
    herolist = Hero_List(hots_db)
    heroclasses = []
    for item in herolist:
        heroclasses.append(Item(item, 'hero'))
    curgame = Game(Team('home'), Team('enemy'), Team('hero_pool', heroclasses), '')
    return curgame

def clear_rating(game_obj):
    for member in game_obj.pool.members:
        member.clr_rating()

def rank_members(game_obj, team_name):
    clear_rating(game_obj)
    team = getattr(game_obj, team_name)
    pool = game_obj.pool
    map = game_obj.map
    for member in pool.members:
        for dimension in dimension_list:
            if getattr(team, dimension) < getattr(map, dimension):
                setattr(member, 'rating', getattr(member, 'rating') + getattr(member, dimension))
            else:
                setattr(member, 'rating', getattr(member, 'rating') + (getattr(member, dimension) * 0.2))
    return game_obj.pool.max_members()

def pick_ban(game_obj, team_name, heroes, pick_type):
    team = getattr(game_obj, team_name)
    if pick_type == '1 pick':
        team.add_hero(game_obj.pool.member(heroes[0]))
        game_obj.pool.remove_hero(heroes[0])
    elif pick_type == '2 picks':
        for hero in heroes:
            team.add_hero(game_obj.pool.member(hero))
            game_obj.pool.remove_hero(hero)
    else:
        team.new_ban(game_obj.pool.member(heroes[0]))
        game_obj.pool.remove_hero(heroes[0])


if __name__ == '__main__':
    gam = game_start()
    cur_map = input('What is the map?')
    gam.map = Item(cur_map, 'map')
    turn = 0
    turns = ['ban', 'ban', 'ban', 'ban', '1 pick', '2 picks', '2 picks', 'ban', 'ban', '2 picks', '2 picks', '1 pick']
    user = input('First or Second?')
    team_swap = {'home_team': 'enemy_team', 'enemy_team': 'home_team'}
    if user == 'First':
        team_turns =[('home_team', turns[x]) if x % 2 == 0 else ('enemy_team', turns[x]) for x in range(0,len(turns))]
    elif user == 'Second':
        team_turns =[('home_team', turns[x]) if x % 2 != 0 else ('enemy_team', turns[x]) for x in range(0,len(turns))]
    while turns:
        if team_turns[turn][1] == 'ban':
            ranks = [item for item in rank_members(gam, team_swap[team_turns[turn][0]])]
        else:
            ranks = [item for item in rank_members(gam, team_turns[turn][0])]
        print('This is a {} round for the {}, here are the best heroes\n{}\n'.format(team_turns[turn][1], team_turns[turn][0], ranks))
        pick = input('What hero(s) were {}?\n'.format(team_turns[turn][1])).split(', ')
        pick_ban(gam, team_turns[turn][0], pick, team_turns[turn][1])
        if turn == 11:
            print('Picking over\nHome Team: {}\nvs\nEnemy Team: {}'.format([hero for hero in gam.home_team.members], [hero for hero in gam.enemy_team.members]))
            break
        print('\nHome Bans: {}  -  Enemy Bans: {}\n'.format([hero for hero in gam.home_team.bans], [hero for hero in gam.enemy_team.bans]))
        print('\nHome Team: {} vs. Enemy Team: {}\n-------------------------\nMoving to next round!\n___________________\n'.format([hero for hero in gam.home_team.members], [hero for hero in gam.enemy_team.members]))
        turn += 1
