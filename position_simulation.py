from velocity_simulation import run_velocity_simulation
from runge_kutta_position import runge_kutta_position
from get_value_at_time import get_value_at_time

velocities = run_velocity_simulation()
velocity_x_list = [v.velocity_x for v in velocities]
velocity_y_list = [v.velocity_y for v in velocities]

class Position:
    def __init__(self, distance, height):
        self.distance = distance
        self.height = height

    def __add__(self, other):
        return Position(self.distance + other.distance, self.height + other.height)

    def __mul__(self, other):
        return Position(self.distance * other, self.height * other)
    
    def __truediv__(self, other):
        return Position(self.distance / other, self.height / other)
    
    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return (f"Position(distance={self.distance}, height={self.height})")
    
    def __repr__(self):
        return self.__str__()
    
def derivative_position(t, dt, velocity_x_list, velocity_y_list):
    d_distance = get_value_at_time(t, dt, velocity_x_list)
    d_height = get_value_at_time(t, dt, velocity_y_list)
    return Position(d_distance, d_height)

def run_position_simulation():
    t = 0
    dt = 0.01
    max_t = 2
    positions = []
    position = Position(distance=0, height=0)
    positions.append(position)
    while t < max_t:
        position = runge_kutta_position(derivative_position, positions[-1], t, dt, velocity_x_list, velocity_y_list)
        positions.append(position)
        t += dt

    for position in positions:
        print(position.distance, ",", position.height)

    return positions
