import enum
from typing import List
import math


class Directions(enum):
    NEG_X = 0    
    POS_X = 1
    NEG_Z = 2
    POS_Z = 3 
    NONE = 4 
    NEG_X_POS_Z = 5
    NEG_X_NEG_Z = 6
    POS_X_POS_Z = 7
    POS_X_NEG_Z = 8

class MinecraftCoordinate(object):
    def __init__(self, x: float, y:float, z: float, heading:float) -> None:
        self._X: float = x
        self._Y: float = y
        self._Z: float = z
        self._heading: float = heading
        self._direction: Directions = Directions.NONE
        self.get_coord_direction()
        self._cart_x = x
        self._cart_y = -1 * z

    
    @property
    def X(self):
        return self._X
    
    @property
    def Y(self):
        return self._Y

    @property
    def Z(self):
        return self._Z
    
    @property
    def cart_coord(self):


    @property
    def heading(self):
        return self._heading

    @property
    def direction(self):
        return self._direction

    def get_coord_direction(self):
        if self._heading > 135 and self._heading < 180:
            self._direction = Directions.NEG_X_NEG_Z
        elif self._heading < -135 and self._heading > -180:
            self._direction = Directions.POS_X_NEG_Z
        elif self._heading > 0 and self._heading < 45:
            self._direction = Directions.NEG_X_POS_Z
        elif self._heading < 0 and self._heading > -45:
            self._direction = Directions.POS_X_POS_Z
        elif self._heading == 135:
            self._direction = Directions.NEG_X
        elif self._heading == 180 or -180:
            self._direction = Directions.NEG_Z
        elif self._heading == -135:
            self._direction = Directions.POS_X
        elif self._heading == 0:
            self._direction = Directions.POS_Z


class StrongholdSprunjer:
    """
    Class for the stronghold sprunjing to happen at
    """
    
    def __init__(self) -> None:
        self._coordinates_list: List[MinecraftCoordinate] = []

    def add_sprunje_line(self, x: float, y:float, z: float, heading:float) :
        coordinate: MinecraftCoordinate = MinecraftCoordinate(x=x,y=y,z=z,heading=heading)
        self._coordinates_list.append(coordinate)

    def triangulate_coordinate_set(self, coord1: MinecraftCoordinate, coord2: MinecraftCoordinate):
        #first find out where coord1 is in relation to coord2
        x_direction_to_coord2: Directions = Directions.NONE
        z_direction_to_coord2: Directions = Directions.NONE
        triangle_point_1: MinecraftCoordinate
        triangle_point_2: MinecraftCoordinate
        triangle_point_3: MinecraftCoordinate


        if coord1.X < coord2.X:
            #it is -x
            triangle_point_1 = coord1
            x_direction_to_coord2 = Directions.POS_X
        elif coord1.X > coord2.X:
            triangle_point_1 = coord2
        elif coord1.X == coord2.X:            
            if coord1.Z < coord2.Z:
                #it is -x
                triangle_point_1 = coord1
                z_direction_to_coord2 = Directions.NEG_Z
            elif coord1.Z > coord2.Z:
                triangle_point_1 = coord2
            elif coord1.Z == coord2.Z:
                raise Exception("both points are the same")

        #now we do actual cartiseian plane stuff so X is x-axis and Y is Y-axis
        point_1_distance_point_2: float = -1
        



    


    


