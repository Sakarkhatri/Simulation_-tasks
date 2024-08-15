import numpy as np
import matplotlib.pyplot as plt

def random_walk_2d(steps):
    x, y = 0, 0
    x_path, y_path = [x], [y]
    
    for _ in range(steps):
        dx, dy = np.random.choice([-1, 1]), np.random.choice([-1, 1])
        x, y = x + dx, y + dy
        x_path.append(x)
        y_path.append(y)
    
    return x_path, y_path

# Simulate the walk
steps = 1000
x_path, y_path = random_walk_2d(steps)

# Plot the path
plt.figure(figsize=(10, 10))
plt.plot(x_path, y_path, 'b-')
plt.plot(x_path[0], y_path[0], 'go', markersize=10, label='Start')
plt.plot(x_path[-1], y_path[-1], 'ro', markersize=10, label='End')
plt.title(f'2D Random Walk ({steps} steps)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()