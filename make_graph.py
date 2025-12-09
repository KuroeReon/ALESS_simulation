import matplotlib.pyplot as plt
from read_config import read_config
from velocity_simulation import run_velocity_simulation
from position_simulation import run_position_simulation

def make_graph(velocities, positions):
    times = [i * read_config().dt for i in range(len(velocities))]

    plt.figure(figsize=(10, 6))

    """plt.subplot(3, 1, 1)
    plt.plot(times, [velocity.velocity_x for velocity in velocities], label="Velocity_X")
    plt.grid(True)
    plt.legend()
    
    plt.subplot(3, 1, 2)
    plt.plot(times, [velocity.velocity_y for velocity in velocities], label="Velocity_Y")
    plt.grid(True)
    plt.legend()"""

    #plt.subplot(3, 1, 3)
    plt.plot([position.distance for position in positions], [position.height for position in positions], label="Position")
    plt.grid(True)
    plt.legend()
    
    plt.show()

make_graph(run_velocity_simulation(), run_position_simulation())