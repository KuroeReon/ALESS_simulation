from dataclasses import dataclass

@dataclass 
class Const:
    gravity: float
    lift_coefficient: float
    drag_coefficient: float
    air_density: float

@dataclass
class Variables:
    wings_area: float
    cross_sectional_area: float
    mass: float
    ini_speed: float
    ini_angle_of_attack: float

    