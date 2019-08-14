class Room:

    pres_wall = 0
    pres_hole = 0
    pres_monster = 0
    pres_gold = 0
    pres_smell = 0
    pres_wind = 0

    num_walls = 0
    num_holes = 0
    num_monsters = 0
    num_gold = 0
    num_smell = 0
    num_wind = 0

    neighbors = []
    isNormal = True


    def __init__(self, id):
        self.id = id
       # self.isNormal = isNormal            # check if normal or border room

    def toString(self):
        if self.isNormal == True:
            return "Room {}, Normal, Monster: {}, Hole: {}, Wall {}, Gold {}, Wind {}, Smell {} \n".format(self.id, self.pres_monster, self.pres_hole, self.pres_wall, self.pres_gold,
                    self.pres_wind, self.pres_smell)
        else:
            return "Room {}, Border, Monster: {}, Hole: {}, Wall {}, Gold {}, Wind {}, Smell {} \n".format(self.id,
                    self.pres_monster, self.pres_hole, self.pres_wall, self.pres_gold, self.pres_wind, self.pres_smell)