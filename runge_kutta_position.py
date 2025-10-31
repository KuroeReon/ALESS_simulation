def runge_kutta_position(derivative, position, t, dt, velocity_x_list, velocity_y_list):    
    k1 = derivative(t, dt, velocity_x_list, velocity_y_list)
    k2 = derivative(t + dt / 2, dt, velocity_x_list, velocity_y_list)
    k3 = derivative(t + dt / 2, dt, velocity_x_list, velocity_y_list)
    k4 = derivative(t + dt, dt, velocity_x_list, velocity_y_list)
    return position + (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6