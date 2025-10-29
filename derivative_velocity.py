import numpy as np

class Velocity:
    def __init__(self, velocity_x, velocity_y):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def __add__(self, other):
        return Velocity(self.velocity_x + other.velocity_x, self.velocity_y + other.velocity_y)

    def __mul__(self, other):
        return Velocity(self.velocity_x * other, self.velocity_y * other)
    
    def __truediv__(self, other):
        return Velocity(self.velocity_x / other, self.velocity_y / other)
    
    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return (f"Velocity(velocity_x={self.velocity_x}, velocity_y={self.velocity_y})")

def velocity_vector(velocity):
    return np.array([velocity.velocity_x, velocity.velocity_y])

def angle_of_attack(velocity):
    return np.arctan(velocity.velocity_y / velocity.velocity_x)

def lift_force(velocity, config):
    return 0.5 * config.air_density * (np.linalg.norm(velocity_vector(velocity)) ** 2) * config.wings_area * config.lift_coefficient

def drag(velocity, config):
    return 0.5 * config.air_density * (np.linalg.norm(velocity_vector(velocity)) ** 2) * config.cross_sectional_area * config.drag_coefficient

def derivative_velocity(velocity, config):
    force_x = - lift_force * np.sin(angle_of_attack(velocity)) + drag * np.cos(angle_of_attack(velocity))
    force_y = lift_force * np.cos(angle_of_attack(velocity)) + drag * np.sin(angle_of_attack(velocity)) - config.mass + config.gravity
    d_velocity_x = force_x / config.mass
    d_velocity_y = force_y / config.mass
    return velocity(d_velocity_y, d_velocity_x)
