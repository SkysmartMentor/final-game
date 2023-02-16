import random

APPLE = 'яблоко'
SWORD = 'меч'
SHIELD = 'щит'
ARROW = 'лук'
CHICKEN = 'курица'

items = (APPLE, SWORD, SHIELD, ARROW, CHICKEN)

POSSIBLE_ITEMS = {
        APPLE: {
            'type': 'eat',
            'name': APPLE,
            'value': random.randint(5, 10),
        },
        SWORD: {
            'type': 'attack',
            'name': SWORD,
            'value': random.randint(20, 100),
        },
        SHIELD: {
            'type': 'defend',
            'name': SHIELD,
            'value': random.randint(10, 50),
        },
        ARROW: {
            'type': 'attack',
            'name': ARROW,
            'value': random.randint(40, 120),
        },
        CHICKEN: {
            'type': 'eat',
            'name': CHICKEN,
            'value': random.randint(20, 30)
        }
    }