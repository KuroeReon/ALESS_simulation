from derivative_velocity import derivative_velocity
from runge_kutta_velocity import runge_kutta_velocity
from get_initial_cartesian_velocity import get_initial_velocity
from read_config import read_config

t = 0

def run_velocity_simulation():
    t = 0
    initial_velocity = get_initial_velocity()
    velocities = []
    velocity = initial_velocity
    velocities.append(velocity)
    config = read_config()
    dt = config.dt
    while t < config.max_t:
        velocity = runge_kutta_velocity(derivative_velocity, velocities[-1], config, dt)
        velocities.append(velocity)
        t += dt
    return velocities