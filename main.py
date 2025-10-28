from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np

class State:
    def __init__(self, velocity_x, velocity_y):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def __add__(self, other):
        return State(self.velocity_x + other.velocity_x, self.velocity_y + other.velocity_y)

    def __mul__(self, other):
        return State(self.velocity_x * other, self.velocity_y * other)
    
    def __truediv__(self, other):
        return State(self.velocity_x / other, self.velocity_y / other)
    
    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return (f"State(velocity_x={self.velocity_x}, velocity_y={self.velocity_y})")

@dataclass 
class Config:
    gravity: float
    wings_area: float
    cross_sectional_area: float
    lift_coefficient: float
    drag_coefficient: float
    air_density: float
    mass: float

def velocity_vector(state):
    return np.array([state.velocity_x, state.velocity_y])

def angle_of_attack(state):
    return np.arctan(state.velocity_y / state.velocity_x)

def lift_force(state, config):
    return 0.5 * config.air_density * (np.linalg.norm(velocity_vector(state)) ** 2) * config.wings_area * config.lift_coefficient

def drag(state, config):
    return 0.5 * config.air_density * (np.linalg.norm(velocity_vector(state)) ** 2) * config.cross_sectional_area * config.drag_coefficient

def derivative(state, config):
    force_x = - lift_force * np.sin(angle_of_attack(state)) + drag * np.cos(angle_of_attack(state))
    force_y = lift_force * np.cos(angle_of_attack(state)) + drag * np.sin(angle_of_attack(state)) - config.mass + config.gravity
    d_velocity_x = force_x / config.mass
    d_velocity_y = force_y / config.mass
    return State(d_velocity_y, d_velocity_x)