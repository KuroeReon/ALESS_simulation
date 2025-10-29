from config import Const

def read_const():
    gravity = -9.8
    lift_coefficient = 0.5
    drag_coefficient = 0.5
    air_density = 1.3
    return Const(gravity, lift_coefficient, drag_coefficient, air_density)