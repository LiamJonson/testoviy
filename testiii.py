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
            print(get_objects_by_coords(i[1]))

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
        print(get_objects_by_coords(i[2]) )
        if get_objects_by_coords(i[2]) :
            k = game_objects[get_objects_by_coords(i[2])[0]]
            print(k)
            if k['interactable'] == True:
                game_objects.update({(i[0],n): k})
            elif k['interactable'] == True:
                pass
            else:
                game_objects.update({(i[0], n): k})



























