import numpy as np

def get_value_at_time(t, dt, data):
    times = np.arange(0, len(data) * dt, dt)
    return np.interp(t, times, data)