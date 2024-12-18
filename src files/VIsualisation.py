# src/visualization.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_path(data, range_label):
    """
    Plots the 3D path for the given trajectory data.

    Args:
        data (numpy.ndarray): Shape (recordings, frames, 3) containing X, Y, Z.
        range_label (str): Label for the range (e.g., Pre-Stimulus, Stimulus).
    """
    mean_path = np.mean(data, axis=0)  # Average trajectory
    x, y, z = mean_path[:, 0], mean_path[:, 1], mean_path[:, 2]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label=range_label, lw=2)
    ax.scatter(x[0], y[0], z[0], color='green', label='Start', s=50)
    ax.scatter(x[-1], y[-1], z[-1], color='red', label='End', s=50)

    ax.set_title(f"3D Path - {range_label}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()

# main.py
import numpy as np
from src.ranging import split_ranges
from src.metrics import calculate_centroid, calculate_path_length, normalize_path_length
from src.visualization import plot_3d_path

# Example usage
position_array = np.random.rand(146, 150, 3)  # Replace with actual data

# Split ranges
pre_stimulus, stimulus, post_stimulus = split_ranges(position_array)

# Calculate metrics
pre_centroid = calculate_centroid(pre_stimulus)
stim_centroid = calculate_centroid(stimulus)
post_centroid = calculate_centroid(post_stimulus)

pre_path_length = calculate_path_length(pre_stimulus)
stim_path_length = calculate_path_length(stimulus)
post_path_length = calculate_path_length(post_stimulus)

# Normalize path lengths
pre_norm_path_length = normalize_path_length(pre_path_length, pre_stimulus.shape[1])
stim_norm_path_length = normalize_path_length(stim_path_length, stimulus.shape[1])
post_norm_path_length = normalize_path_length(post_path_length, post_stimulus.shape[1])

# Print metrics
print("Pre-Stimulus Centroid:", pre_centroid)
print("Stimulus Centroid:", stim_centroid)
print("Post-Stimulus Centroid:", post_centroid)

print("Pre-Stimulus Path Length:", pre_path_length)
print("Stimulus Path Length:", stim_path_length)
print("Post-Stimulus Path Length:", post_path_length)

print("Normalized Path Lengths:")
print("Pre-Stimulus:", pre_norm_path_length)
print("Stimulus:", stim_norm_path_length)
print("Post-Stimulus:", post_norm_path_length)

# Visualize paths
plot_3d_path(pre_stimulus, "Pre-Stimulus")
plot_3d_path(stimulus, "Stimulus")
plot_3d_path(post_stimulus, "Post-Stimulus")
