from config import Config
import math

def read_config():
    gravity = 9.8
    air_density = 1.3
    wings_area = 0.0094111
    mass = 0.050
    ini_speed = 2.9098 #small
    #middleだと2.50446
    ini_angle_of_attack = math.pi / 6
    max_t = 100
    dt = 0.01
    return Config(gravity, air_density, wings_area,
                  mass, ini_speed, ini_angle_of_attack, max_t, dt)