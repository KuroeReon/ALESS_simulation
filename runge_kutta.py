#Runge-Kutta法による常微分方程式の数値解析

def runge_kutta(derivative, state, config, dt):    
    k1 = derivative(state, config)
    k2 = derivative(state + k1 * dt / 2, config)
    k3 = derivative(state + k2 * dt / 2, config)
    k4 = derivative(state + k3 * dt, config)
    return state + (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6