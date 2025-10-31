from derivative_velocity import Velocity, derivative_velocity
from runge_kutta import runge_kutta
from get_initial_cartesian_velocity import get_initial_velocity
from read_config import read_config

initial_velocity = get_initial_velocity()

t = 0
dt = 0.01
max_t = 1
const = read_config()

def run_velocity_simulation(initial_velocity, t, dt, max_t, derivative_velocity):
    velocities = []
    velocity = initial_velocity
    velocities.append(velocity)
    while t < max_t:
        velocity = runge_kutta(derivative_velocity, velocities[-1], const, dt)
        velocities.append(velocity)
        t += dt
    return velocities

print(run_velocity_simulation(initial_velocity, t, dt, max_t, derivative_velocity))