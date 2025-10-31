from dataclasses import dataclass

@dataclass 
class Config:
    gravity: float
    lift_coefficient: float
    drag_coefficient: float
    air_density: float
    wings_area: float
    cross_sectional_area: float
    mass: float
    ini_speed: float
    ini_angle_of_attack: float
    max_t: float
    dt: float

    