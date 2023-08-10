import matplotlib.pyplot as plt
import numpy as np

# Simulate migratory bird tracking data
num_birds = 5
num_time_steps = 50
bird_data = []

for _ in range(num_birds):
    bird_trajectory = []
    x, y = np.random.randint(0, 100), np.random.randint(0, 100)
    bird_trajectory.append((x, y))
    
    for _ in range(num_time_steps - 1):
        x += np.random.randint(-5, 6)
        y += np.random.randint(-5, 6)
        bird_trajectory.append((x, y))
    
    bird_data.append(bird_trajectory)

# Plot migratory bird trajectories
plt.figure(figsize=(10, 6))
for i in range(num_birds):
    bird_trajectory = np.array(bird_data[i])
    plt.plot(bird_trajectory[:, 0], bird_trajectory[:, 1], label=f'Bird {i + 1}')

plt.title("Migratory Bird Tracking")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.legend()
plt.grid()
plt.show()
