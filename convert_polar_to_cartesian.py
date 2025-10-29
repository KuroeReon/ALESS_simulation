import numpy as np
from derivative_velocity import Velocity

class Velocity_polar:
    def __init__(self, speed, angle_of_attack):
        self.ini_speed = speed
        self.ini_angle_of_attack = angle_of_attack

def covert_polar_velocity_to_cartesian(velocity_polar):
    velocity_x = velocity_polar.inispeed * np.cos(velocity_polar.angle_of_attack)
    velocity_y = velocity_polar.inispeed * np.sin(velocity_polar.angle_of_attack)
    return Velocity(velocity_x, velocity_y)