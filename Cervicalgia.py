import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define unique coordinates for each vertex based on the uploaded image
coordinates = [
    (58.5, 170), (51, 120), (58.06, 61.9), (58.06, 19),
    (48.84, 19), (54.44, -9.5), (44.44, -35.9),(48.71, 19.9)
]

coords = np.array(coordinates)

star_indices = [2,3]

star_color = '#FFFF00'
star_edge_color = '#FFA500'
line_color = '#FFD700'
glow_color = '#FFFF99'
boundary_color = '#00FF00'  # Color for the faint boundary around the constellation

np.random.seed(0)
num_background_stars = 500
bg_x = np.random.uniform(40, 100, num_background_stars)
bg_y = np.random.uniform(-60, 180, num_background_stars)
bg_sizes = np.random.uniform(0.1, 1.5, num_background_stars)

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(40, 100)
ax.set_ylim(-60, 180)
plt.gca().invert_yaxis()
plt.axis('off')

bg_stars = ax.scatter(bg_x, bg_y, color='white', s=bg_sizes, alpha=0.3, zorder=0)

# Draw lines between stars with a smoother glow effect
for i in range(len(coords) - 1):
    ax.plot([coords[i, 0], coords[i + 1, 0]], [coords[i, 1], coords[i + 1, 1]], color=line_color, lw=2, zorder=2)
    for glow_size in [3, 5, 7]:
        ax.plot([coords[i, 0], coords[i + 1, 0]], [coords[i, 1], coords[i + 1, 1]], color=glow_color, lw=glow_size, alpha=0.05, zorder=1)

# Plot stars with a glow effect and a yellow-orange border
stars = []
for i, (x, y) in enumerate(coords):
    size = 300 if i in star_indices else 50
    star = ax.scatter(x, y, color=star_color, s=size, edgecolor=star_edge_color, linewidth=2, alpha=0.9, zorder=4)
    stars.append(star)

glow_circles = []
for i, (x, y) in enumerate(coords):
    glow_size = 600 if i in star_indices else 100
    glow_circle = ax.scatter(x, y, color=star_color, s=glow_size, edgecolor='none', alpha=0.1, zorder=3)
    glow_circles.append(glow_circle)

boundary_x = [coordinates[i][0] for i in range(len(coordinates))]
boundary_y = [coordinates[i][1] for i in range(len(coordinates))]
ax.plot(boundary_x, boundary_y, color=boundary_color, lw=0.5, linestyle='--', alpha=0.5, zorder=1)

def update(frame):
    # Twinkling
    bg_alpha = np.random.uniform(0.1, 0.6, num_background_stars)
    bg_stars.set_alpha(bg_alpha)
    
    for i in star_indices:
        alpha = np.random.uniform(0.6, 1.0)
        stars[i].set_alpha(alpha)
    
    return [bg_stars] + stars

ani = FuncAnimation(fig, update, frames=200, interval=180, blit=True)
plt.show()