from base_classes import Map, Hero, Item, Team


a = Hero('Hanzo')
a.waveclear = 200
a.movement = 110
a.camps = 180
a.dmg = 170
a.tank = 60
a.support = 20

b = Hero('Lucio')
b.waveclear = 30
b.movement = 150
b.camps = 20
b.dmg = 30
b.tank = 20
b.support = 300

c = Hero('Orphea')
c.waveclear = 200
c.movement = 80
c.camps = 60
c.dmg = 200
c.tank = 70
c.support = 20

d = Hero('ETC')
d.waveclear = 100
d.movement = 200
d.camps = 60
d.dmg = 70
d.tank = 300
d.support = 50

e = Hero('Sylvanas')
e.waveclear = 180
e.movement = 130
e.camps = 200
e.dmg = 110
e.tank = 40
e.support = 20

f = Map('Braxis Holdout', 'double-point')
f.waveclear = 180
f.movement = 130
f.camps = 200


d = Team()
for heroes in [a, b, c, d, e]:
    d.add_hero(heroes)

print(d)
