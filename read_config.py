from config import Config

def read_config():
    gravity = 9.8
    lift_coefficient = 0.5
    drag_coefficient = 0.5
    air_density = 1.3
    wings_area = 0.02
    cross_sectional_area = 0.00001
    mass = 0.005
    ini_speed = 2
    ini_angle_of_attack = 3.14 / 6
    max_t = 1
    dt = 0.01
    return Config(gravity, lift_coefficient, drag_coefficient, air_density, wings_area,
                  cross_sectional_area, mass, ini_speed, ini_angle_of_attack, max_t, dt)