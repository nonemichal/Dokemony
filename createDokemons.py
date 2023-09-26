def create():
    class Attacks:
        def __init__(self, name, typ1, typ2, dmg_min, dmg_max):
            self.name = name
            '''attack, special attack lub status'''
            self.typ1 = typ1
            '''typ żywiołu'''
            self.typ2 = typ2
            self.dmg_min = dmg_min
            self.dmg_max = dmg_max

    attacks = []
    attacks.append(Attacks('Punch', 'attack', 'normal', 20, 30))
    attacks.append(Attacks('Slow down', 'status', 'normal', 0, 0))
    attacks.append(Attacks('Defence reduction', 'status', 'normal', 0, 0))
    attacks.append(Attacks('Attack reduction', 'status', 'normal', 0, 0))
    attacks.append(Attacks('Heal', 'status', 'normal', 0, 0))
    attacks.append(Attacks('Thunder', 'special_attack', 'electric', 10, 30))
    attacks.append(Attacks('Fire', 'special_attack', 'fire', 20, 30))
    attacks.append(Attacks('Grass', 'special_attack', 'grass', 15, 30))
    attacks.append(Attacks('Water', 'special_attack', 'water', 20, 25))
    attacks.append(Attacks('Earth', 'special_attack', 'ground', 20, 50))
    attacks.append(Attacks('Air', 'special_attack', 'flying', 15, 30))


    class Dokemon:
        def __init__(self, name, health, speed, attack, special_attack, defense, special_defense, typ, attack1, attack2, attack3, attack4, sprite):
            self.name = name
            self.health = health
            self.max_health = health
            self.attack = attack
            self.special_attack = special_attack
            self.typ = typ
            self.speed = speed
            self.defense = defense
            self.special_defense = special_defense
            self.attack1 = attack1
            self.attack2 = attack2
            self.attack3 = attack3
            self.attack4 = attack4
            self.sprite = sprite

    dokemons = []
    dokemons.append(Dokemon('Pikachu', 80, 140, 60, 100, 10, 30,
                    'electric', attacks[0], attacks[3], attacks[5], attacks[4], 'pikachu.png'))
    dokemons.append(Dokemon('Charmander', 90, 100, 90, 80, 20, 20,
                    'fire', attacks[0], attacks[2], attacks[6], attacks[4], 'charmander.png'))
    dokemons.append(Dokemon('Bulbasaur', 100, 80, 70, 80, 30, 30,
                    'grass', attacks[0], attacks[1], attacks[7], attacks[4], 'bulbasaur.png'))
    dokemons.append(Dokemon('Squirtle', 90, 90, 70, 100, 20, 35,
                    'water', attacks[0], attacks[1], attacks[8], attacks[4], 'squirtle.png'))
    dokemons.append(Dokemon('Sandslash', 90, 60, 80, 50, 40, 10, 'ground',
                    attacks[0], attacks[2], attacks[9], attacks[4], 'sands.png'))
    dokemons.append(Dokemon('Aerodactyl', 70, 150, 100, 80, 20, 20,
                    'flying', attacks[0], attacks[3], attacks[10], attacks[4], 'aerodactyl.png'))
    
    return dokemons
