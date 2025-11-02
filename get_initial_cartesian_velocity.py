from convert_polar_to_cartesian import Velocity_polar, convert_polar_velocity_to_cartesian
from read_config import read_config

ini_speed = read_config().ini_speed
ini_angle_of_attack = read_config().ini_angle_of_attack

def get_initial_velocity():
    initial_velocity = Velocity_polar(ini_speed, ini_angle_of_attack)
    return convert_polar_velocity_to_cartesian(initial_velocity)
