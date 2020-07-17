game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'},
    ('coin', 2): {'position': (1, 2), 'passable': True, 'interactable': True, 'char': '$'}
}

interactions =[]
old_objects = []


def get_objects_by_coords(position):
    n = []
    for i,j in game_objects.items():
        if j['position'] == position:
            n.append(i)
    return n

def remove_objects():
    for i in old_objects:
        if game_objects.get(i):
            del game_objects[i]
    old_objects.clear()

def idle_interaction(o1, o2):
    pass

def process_interactions():
    for obj1, obj2 in interactions:
        interaction_funs.get(obj1[0], idle_interaction)(obj1, obj2)
        interaction_funs.get(obj2[0], idle_interaction)(obj2, obj1)
    interactions.clear()

def player_interaction(player, obj):
    if 'coin' in obj:
        old_objects.append(obj)

def wave_interaction(wave, obj):
    if 'soft_wall' in obj or 'player' in obj:
        old_objects.append(obj)

interaction_funs = {
    'player': player_interaction,
    'heatwave': wave_interaction,
}

def move_objects():
    for i in movements:
        p = get_objects_by_coords(i[1])
        if p:
            if game_objects[p[0]]['passable']== True:
                if game_objects[p[0]]['interactable'] == True:
                    interactions.append(((i[0]), (*p)))
                    game_objects[i[0]].update({'position': i[1]})
                else:
                    game_objects[i[0]].update({'position': i[1]})

        elif not p:
            game_objects[i[0]].update({'position': i[1]})
    movements.clear()

movements = []
objects_ids_counter = 0

def get_next_counter_value():
    global objects_ids_counter
    result = objects_ids_counter
    objects_ids_counter += 1
    return result

new_objects = []


def add_new_objects():
    for i in new_objects:
        n = get_next_counter_value()
        k = i[1]
        k.update({'position': i[2]})
        if get_objects_by_coords(i[-1]):
            k = game_objects[get_objects_by_coords(i[-1])[0]]
            if k['interactable'] == True:
                game_objects.update({(i[0],n): k})
        else:
            game_objects.update({(i[0], n): k})


obj_types_to_char = {
    "player": "@", "wall": '#', 'soft_wall': '%', 'heatwave': '+', "bomb": '*', "coin": '$'
}


def create_object(type, position, **kwargs):
    desc = {'position': position,
            'passable': type not in ['wall', 'soft_wall'],
            'interactable': type not in ['wall'],
            'char': obj_types_to_char[type]
            }
    if type == 'player':
        desc['coins'] = 0
    if type == 'bomb':
        desc['power'] = 3
        desc['life_time'] = 3
    desc.update(kwargs)
    return type, desc, position

def load_level(level):
    game_objects.clear()
    n = [i for i in level.strip().split('\n')]
    m = {j: i for i, j in obj_types_to_char.items()}
    for i,j in enumerate(n):
        for k, l in enumerate(j):
            if l == ' ':
                continue
            else:
                new_objects.append((create_object(m[l], (i, k))))
    add_new_objects()
    print(game_objects)

level_example = """
##########
#@ *%    #
#   %    #
#  %%%   #
# %%$%%  #
#  %%%   #
#   %    #
#   %    #
#   %    #
##########
"""

load_level(level_example)

def idle_logic(_):
    pass


def bomb_logic(bomb_object):
    for game_object in game_objects:
        if game_object[0] == 'bomb':
            if game_objects[game_object]['life_time'] != 0:
                game_objects[game_object]['life_time'] -= 1
            else:
                old_objects.append(game_object)
                n = game_objects[game_object]['position']
                new_objects.append(('heatwave', {'passable': True, 'interactable': True, },(n[0],n[1]-1)))
                new_objects.append(('heatwave', {'passable': True, 'interactable': True, }, (n[0]-1, n[1])))
                new_objects.append(('heatwave', {'passable': True, 'interactable': True, }, (n[0], n[1])))
                new_objects.append(('heatwave', {'passable': True, 'interactable': True, }, (n[0], n[1] + 1)))
                new_objects.append(('heatwave', {'passable': True, 'interactable': True, }, (n[0]+1 , n[1])))




new_objects = [('bomb', {'passable': True, 'interactable': True, 'lifetime': 5}, (1, 1))]

def heatwave_logic(heatwave):
    for game_object in game_objects:
        if game_object[0] == 'heatwave':
            old_objects.append(game_object)


object_logics = {
    'bomb': bomb_logic,
    'heatwave': heatwave_logic
}


def process_objects_logic():
    for game_object in game_objects:
        object_logics.get(game_object[0], idle_logic)(game_object)

process_objects_logic()
assert all(t == 'heatwave' for t, desc, pos in new_objects)





















