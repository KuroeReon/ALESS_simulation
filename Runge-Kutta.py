#Runge-Kutta法による常微分方程式の数値解析

def runge_kutta(derivative, state, config, t, dt, mass, thrust):    
    k1 = derivative(state, config, mass, thrust, t, dt)
    k2 = derivative(state + k1 * dt / 2, config, mass, thrust, t + dt / 2, dt)
    k3 = derivative(state + k2 * dt / 2, config, mass, thrust, t + dt / 2, dt)
    k4 = derivative(state + k3 * dt, config, mass, thrust, t + dt, dt)
    return state + (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6