import numpy as np
from derivative_velocity import Velocity

class Velocity_polar:
    def __init__(self, speed, angle_of_attack):
        self.speed = speed
        self.angle_of_attack = angle_of_attack

def convert_polar_velocity_to_cartesian(velocity_polar):
    velocity_x = velocity_polar.speed * np.cos(velocity_polar.angle_of_attack)
    velocity_y = velocity_polar.speed * np.sin(velocity_polar.angle_of_attack)
    return Velocity(velocity_x, velocity_y)