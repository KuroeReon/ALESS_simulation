from config import Variables

def read_variables():
    wings_area = 500
    cross_sectional_area = 20
    mass = 20
    ini_speed = 10
    ini_angle_of_attack = 10
    return Variables(wings_area, cross_sectional_area, mass, ini_speed, ini_angle_of_attack)