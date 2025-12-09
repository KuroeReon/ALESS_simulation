from dataclasses import dataclass

@dataclass 
class Config:
    gravity: float
    air_density: float
    wings_area: float
    mass: float
    ini_speed: float
    ini_angle_of_attack: float
    max_t: float
    dt: float

    