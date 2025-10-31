from derivative_veocity import Velocity, derivative_velocity
from Runge-Kutta import runge_kutta

def run_simulation(config, initial_state, t, dt, max_t, states, thrust, mass):
    state = initial_state
    states.append(state)
    while t < max_t and state.height >= 0:
        state = runge_kutta(derivative, states[-1], config, t, dt, mass, thrust)
        states.append(state)
        t += dt

main()