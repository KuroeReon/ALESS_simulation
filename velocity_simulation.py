from derivative_veocity import Velocity, derivative_velocity
from Runge-Kutta import runge_kutta
from get_initial_cartesian_velocity import get_initial_velocity

initial_velocity = get_initial_velocity

t = 100
dt = 0.01

def run_velocity_simulation(initial_velocity, t, dt, max_t, derivative_velocity):
    velocities = []
    velocity = initial_velocity
    velocities.append(velocity)
    while t < max_t:
        velocity = runge_kutta(derivative_velocity, velocities[-1], t, dt)
        velocities.append(velocity)
        t += dt
    return velocities